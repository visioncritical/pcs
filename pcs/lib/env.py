from pcs.common.node_communicator import NodeCommunicatorFactory
from pcs.common.tools import Version
from pcs.lib import reports
from pcs.lib.booth.env import BoothEnv
from pcs.lib.cib.tools import get_cib_crm_feature_set
from pcs.lib.node import get_existing_nodes_names
from pcs.lib.pacemaker.env import PacemakerEnv
from pcs.lib.communication import qdevice
from pcs.lib.communication.corosync import (
    CheckCorosyncOffline,
    DistributeCorosyncConf,
    ReloadCorosyncConf,
)
from pcs.lib.communication.tools import (
    run,
    run_and_raise,
)
from pcs.lib.corosync.config_facade import ConfigFacade as CorosyncConfigFacade
from pcs.lib.corosync.config_parser import (
    verify_section as verify_corosync_section
)
from pcs.lib.corosync.live import get_local_corosync_conf
from pcs.lib.external import CommandRunner
from pcs.lib.errors import LibraryError
from pcs.lib.node_communication import (
    LibCommunicatorLogger,
    NodeTargetLibFactory,
)
from pcs.lib.pacemaker.live import (
    diff_cibs_xml,
    ensure_cib_version,
    ensure_wait_for_idle_support,
    get_cib,
    get_cib_xml,
    get_cluster_status_xml,
    push_cib_diff_xml,
    replace_cib_configuration,
    wait_for_idle,
)
from pcs.lib.pacemaker.state import get_cluster_state_dom
from pcs.lib.pacemaker.values import get_valid_timeout_seconds
from pcs.lib.tools import write_tmpfile
from pcs.lib.xml_tools import etree_to_str

MIN_FEATURE_SET_VERSION_FOR_DIFF = Version(3, 0, 9)

class LibraryEnvironment:
    # pylint: disable=too-many-instance-attributes, too-many-public-methods

    def __init__(
        self,
        logger,
        report_processor,
        user_login=None,
        user_groups=None,
        cib_data=None,
        corosync_conf_data=None,
        booth=None,
        known_hosts_getter=None,
        request_timeout=None,
    ):
        # pylint: disable=too-many-arguments
        self._logger = logger
        self._report_processor = report_processor
        self._user_login = user_login
        self._user_groups = [] if user_groups is None else user_groups
        self._cib_data = cib_data
        self._corosync_conf_data = corosync_conf_data
        self._booth = (
            BoothEnv(report_processor, booth) if booth is not None else None
        )
        #pacemaker is currently not mocked and it provides only an access to
        #the authkey
        self._pacemaker = PacemakerEnv()
        self._request_timeout = request_timeout
        # TODO tokens probably should not be inserted from outside, but we're
        # postponing dealing with them, because it's not that easy to move
        # related code currently - it's in pcsd
        self._known_hosts_getter = known_hosts_getter
        self._known_hosts = None
        self._cib_upgrade_reported = False
        self._cib_data_tmp_file = None
        self.__loaded_cib_diff_source = None
        self.__loaded_cib_diff_source_feature_set = None
        self.__loaded_cib_to_modify = None
        self._communicator_factory = NodeCommunicatorFactory(
            LibCommunicatorLogger(self.logger, self.report_processor),
            self.user_login,
            self.user_groups,
            self._request_timeout
        )

        self.__timeout_cache = {}

    @property
    def logger(self):
        return self._logger

    @property
    def report_processor(self):
        return self._report_processor

    @property
    def user_login(self):
        return self._user_login

    @property
    def user_groups(self):
        return self._user_groups

    def get_cib(self, minimal_version=None):
        if self.__loaded_cib_diff_source is not None:
            raise AssertionError("CIB has already been loaded")
        self.__loaded_cib_diff_source = get_cib_xml(self.cmd_runner())
        self.__loaded_cib_to_modify = get_cib(self.__loaded_cib_diff_source)
        if minimal_version is not None:
            upgraded_cib = ensure_cib_version(
                self.cmd_runner(),
                self.__loaded_cib_to_modify,
                minimal_version
            )
            if upgraded_cib is not None:
                self.__loaded_cib_to_modify = upgraded_cib
                self.__loaded_cib_diff_source = etree_to_str(upgraded_cib)
                if not self._cib_upgrade_reported:
                    self.report_processor.process(
                        reports.cib_upgrade_successful()
                    )
                self._cib_upgrade_reported = True
        self.__loaded_cib_diff_source_feature_set = (
            get_cib_crm_feature_set(
                self.__loaded_cib_to_modify,
                none_if_missing=True
            )
            or
            Version(0, 0, 0)
        )
        return self.__loaded_cib_to_modify

    @property
    def cib(self):
        if self.__loaded_cib_diff_source is None:
            raise AssertionError("CIB has not been loaded")
        return self.__loaded_cib_to_modify

    def get_cluster_state(self):
        return get_cluster_state_dom(get_cluster_status_xml(self.cmd_runner()))

    def get_wait_timeout(self, wait):
        if wait is False:
            return False

        if wait not in self.__timeout_cache:
            if not self.is_cib_live:
                raise LibraryError(reports.wait_for_idle_not_live_cluster())
            ensure_wait_for_idle_support(self.cmd_runner())
            self.__timeout_cache[wait] = get_valid_timeout_seconds(wait)
        return self.__timeout_cache[wait]


    def ensure_wait_satisfiable(self, wait):
        """
        Raise when wait is not supported or when wait is not valid wait value.

        mixed wait can be False when waiting is not required or valid timeout
        """
        self.get_wait_timeout(wait)

    def push_cib(self, custom_cib=None, wait=False):
        """
        Push previously loaded instance of CIB or a custom CIB

        etree custom_cib -- push a custom CIB instead of a loaded instance
            (allows to push an externally provided CIB and replace the one in
            the cluster completely)
        mixed wait -- how many seconds to wait for pacemaker to process new CIB
            or False for not waiting at all
        """
        if custom_cib is not None:
            if self.__loaded_cib_diff_source is not None:
                raise AssertionError(
                    "CIB has been loaded, cannot push custom CIB"
                )
            return self.__push_cib_full(custom_cib, wait)
        if self.__loaded_cib_diff_source is None:
            raise AssertionError("CIB has not been loaded")
        # Push by diff works with crm_feature_set > 3.0.8, see
        # https://bugzilla.redhat.com/show_bug.cgi?id=1488044 for details. We
        # only check the version if a CIB has been loaded, otherwise the push
        # fails anyway. By my testing it seems that only the source CIB's
        # version matters.
        if(
            self.__loaded_cib_diff_source_feature_set
            <
            MIN_FEATURE_SET_VERSION_FOR_DIFF
        ):
            self.report_processor.process(
                reports.cib_push_forced_full_due_to_crm_feature_set(
                    MIN_FEATURE_SET_VERSION_FOR_DIFF,
                    self.__loaded_cib_diff_source_feature_set
                )
            )
            return self.__push_cib_full(self.__loaded_cib_to_modify, wait=wait)
        return self.__push_cib_diff(wait=wait)

    def __push_cib_full(self, cib_to_push, wait=False):
        cmd_runner = self.cmd_runner()
        self.__do_push_cib(
            cmd_runner,
            lambda: replace_cib_configuration(cmd_runner, cib_to_push),
            wait
        )

    def __push_cib_diff(self, wait=False):
        cmd_runner = self.cmd_runner()
        self.__do_push_cib(
            cmd_runner,
            lambda: self.__main_push_cib_diff(cmd_runner),
            wait
        )

    def __main_push_cib_diff(self, cmd_runner):
        cib_diff_xml = diff_cibs_xml(
            cmd_runner,
            self.report_processor,
            self.__loaded_cib_diff_source,
            etree_to_str(self.__loaded_cib_to_modify)
        )
        if cib_diff_xml:
            push_cib_diff_xml(cmd_runner, cib_diff_xml)

    def __do_push_cib(self, cmd_runner, push_strategy, wait):
        timeout = self.get_wait_timeout(wait)
        push_strategy()
        self._cib_upgrade_reported = False
        self.__loaded_cib_diff_source = None
        self.__loaded_cib_diff_source_feature_set = None
        self.__loaded_cib_to_modify = None
        if self.is_cib_live and timeout is not False:
            wait_for_idle(cmd_runner, timeout)

    @property
    def is_cib_live(self):
        return self._cib_data is None

    @property
    def final_mocked_cib_content(self):
        if self.is_cib_live:
            raise AssertionError(
                "Final mocked cib content does not make sense in live env."
            )

        if self._cib_data_tmp_file:
            self._cib_data_tmp_file.seek(0)
            return self._cib_data_tmp_file.read()

        return self._cib_data


    def get_corosync_conf_data(self):
        if self._corosync_conf_data is None:
            return get_local_corosync_conf()
        return self._corosync_conf_data

    def get_corosync_conf(self):
        return CorosyncConfigFacade.from_string(self.get_corosync_conf_data())

    def push_corosync_conf(
        self, corosync_conf_facade, skip_offline_nodes=False
    ):
        bad_sections, bad_attr_names, bad_attr_values = verify_corosync_section(
            corosync_conf_facade.config
        )
        if bad_sections or bad_attr_names or bad_attr_values:
            raise LibraryError(
                reports.corosync_config_cannot_save_invalid_names_values(
                    bad_sections, bad_attr_names, bad_attr_values
                )
            )
        corosync_conf_data = corosync_conf_facade.config.export()
        if self.is_corosync_conf_live:
            node_name_list, report_list = get_existing_nodes_names(
                corosync_conf_facade,
                # Pcs is unable to communicate with nodes missing names. It
                # cannot send new corosync.conf to them. That might break the
                # cluster. Hence we error out.
                error_on_missing_name=True
            )
            self.report_processor.process_list(report_list)

            self._push_corosync_conf_live(
                self.get_node_target_factory().get_target_list(
                    node_name_list,
                    skip_non_existing=skip_offline_nodes,
                ),
                corosync_conf_data,
                corosync_conf_facade.need_stopped_cluster,
                corosync_conf_facade.need_qdevice_reload,
                skip_offline_nodes,
            )
        else:
            self._corosync_conf_data = corosync_conf_data

    def _push_corosync_conf_live(
        self, target_list, corosync_conf_data, need_stopped_cluster,
        need_qdevice_reload, skip_offline_nodes
    ):
        # Check if the cluster is stopped when needed
        if need_stopped_cluster:
            com_cmd = CheckCorosyncOffline(
                self.report_processor, skip_offline_nodes
            )
            com_cmd.set_targets(target_list)
            run_and_raise(self.get_node_communicator(), com_cmd)
        # Distribute corosync.conf
        com_cmd = DistributeCorosyncConf(
            self.report_processor, corosync_conf_data, skip_offline_nodes
        )
        com_cmd.set_targets(target_list)
        run_and_raise(self.get_node_communicator(), com_cmd)
        # Reload corosync
        if not need_stopped_cluster:
            # If cluster must be stopped then we cannot reload corosync because
            # the cluster is stopped. If it is not stopped, we do not even get
            # here.
            com_cmd = ReloadCorosyncConf(self.report_processor)
            com_cmd.set_targets(target_list)
            run_and_raise(self.get_node_communicator(), com_cmd)
        # Reload qdevice if needed
        if need_qdevice_reload:
            self.report_processor.process(
                reports.qdevice_client_reload_started()
            )
            com_cmd = qdevice.Stop(self.report_processor, skip_offline_nodes)
            com_cmd.set_targets(target_list)
            run(self.get_node_communicator(), com_cmd)
            report_list = com_cmd.error_list
            com_cmd = qdevice.Start(self.report_processor, skip_offline_nodes)
            com_cmd.set_targets(target_list)
            run(self.get_node_communicator(), com_cmd)
            report_list += com_cmd.error_list
            if report_list:
                raise LibraryError()

    @property
    def is_corosync_conf_live(self):
        return self._corosync_conf_data is None

    def cmd_runner(self):
        runner_env = {
            # make sure to get output of external processes in English and ASCII
            "LC_ALL": "C",
        }

        if self.user_login:
            runner_env["CIB_user"] = self.user_login

        if not self.is_cib_live:
            # Dump CIB data to a temporary file and set it up in the runner.
            # This way every called pacemaker tool can access the CIB and we
            # don't need to take care of it every time the runner is called.
            if not self._cib_data_tmp_file:
                try:
                    cib_data = self._cib_data
                    self._cib_data_tmp_file = write_tmpfile(cib_data)
                    self.report_processor.process(
                        reports.tmp_file_write(
                            self._cib_data_tmp_file.name,
                            cib_data
                        )
                    )
                except EnvironmentError as e:
                    raise LibraryError(reports.cib_save_tmp_error(str(e)))
            runner_env["CIB_file"] = self._cib_data_tmp_file.name

        return CommandRunner(self.logger, self.report_processor, runner_env)

    @property
    def communicator_factory(self):
        return self._communicator_factory

    def get_node_communicator(self, request_timeout=None):
        return self.communicator_factory.get_communicator(
            request_timeout=request_timeout
        )

    def get_node_target_factory(self):
        return NodeTargetLibFactory(
            self.__get_known_hosts(), self.report_processor
        )

    def get_known_hosts(self, host_name_list):
        known_hosts = self.__get_known_hosts()
        return [
            known_hosts[host_name]
            for host_name in host_name_list
            if host_name in known_hosts
        ]

    def __get_known_hosts(self):
        if self._known_hosts is None:
            if self._known_hosts_getter:
                self._known_hosts = self._known_hosts_getter()
            else:
                self._known_hosts = {}
        return self._known_hosts

    @property
    def booth(self):
        return self._booth

    @property
    def pacemaker(self):
        return self._pacemaker
