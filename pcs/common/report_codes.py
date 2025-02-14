# pylint: disable=line-too-long

# force categories
FORCE = "FORCE"
FORCE_ALERT_RECIPIENT_VALUE_NOT_UNIQUE = "FORCE_ALERT_RECIPIENT_VALUE_NOT_UNIQUE"
FORCE_ALREADY_IN_CLUSTER = "FORCE_ALREADY_IN_CLUSTER"
FORCE_BOOTH_DESTROY = "FORCE_BOOTH_DESTROY"
FORCE_BOOTH_REMOVE_FROM_CIB = "FORCE_BOOTH_REMOVE_FROM_CIB"
FORCE_REMOVE_MULTIPLE_NODES = "FORCE_REMOVE_MULTIPLE_NODES"
FORCE_CONSTRAINT_DUPLICATE = "FORCE_CONSTRAINT_DUPLICATE"
FORCE_CONSTRAINT_MULTIINSTANCE_RESOURCE = "FORCE_CONSTRAINT_MULTIINSTANCE_RESOURCE"
FORCE_FILE_OVERWRITE = "FORCE_FILE_OVERWRITE"
FORCE_LOAD_NODES_FROM_CIB = "FORCE_LOAD_NODES_FROM_CIB"
FORCE_LOAD_THRESHOLD = "FORCE_LOAD_THRESHOLD"
FORCE_METADATA_ISSUE = "FORCE_METADATA_ISSUE"
FORCE_NODE_ADDRESSES_UNRESOLVABLE = "FORCE_NODE_ADDRESSES_UNRESOLVABLE"
FORCE_NODE_DOES_NOT_EXIST = "FORCE_NODE_DOES_NOT_EXIST"
FORCE_OPTIONS = "FORCE_OPTIONS"
FORCE_QDEVICE_MODEL = "FORCE_QDEVICE_MODEL"
FORCE_QDEVICE_USED = "FORCE_QDEVICE_USED"
FORCE_QUORUM_LOSS = "FORCE_QUORUM_LOSS"
FORCE_STONITH_RESOURCE_DOES_NOT_EXIST = "FORCE_STONITH_RESOURCE_DOES_NOT_EXIST"
FORCE_NOT_SUITABLE_COMMAND = "FORCE_NOT_SUITABLE_COMMAND"
FORCE_CLEAR_CLUSTER_NODE = "FORCE_CLEAR_CLUSTER_NODE"
FORCE_RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE = "FORCE_RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE"
SKIP_OFFLINE_NODES = "SKIP_OFFLINE_NODES"
SKIP_FILE_DISTRIBUTION_ERRORS = "SKIP_FILE_DISTRIBUTION_ERRORS"
SKIP_ACTION_ON_NODES_ERRORS = "SKIP_ACTION_ON_NODES_ERRORS"
SKIP_UNREADABLE_CONFIG = "SKIP_UNREADABLE_CONFIG"

AGENT_NAME_GUESS_FOUND_MORE_THAN_ONE = "AGENT_NAME_GUESS_FOUND_MORE_THAN_ONE"
AGENT_NAME_GUESS_FOUND_NONE = "AGENT_NAME_GUESS_FOUND_NONE"
AGENT_NAME_GUESSED = "AGENT_NAME_GUESSED"
BAD_CLUSTER_STATE_FORMAT = 'BAD_CLUSTER_STATE_FORMAT'
BOOTH_ADDRESS_DUPLICATION = "BOOTH_ADDRESS_DUPLICATION"
BOOTH_ALREADY_IN_CIB = "BOOTH_ALREADY_IN_CIB"
BOOTH_CANNOT_DETERMINE_LOCAL_SITE_IP = "BOOTH_CANNOT_DETERMINE_LOCAL_SITE_IP"
BOOTH_CANNOT_IDENTIFY_KEYFILE = "BOOTH_CANNOT_IDENTIFY_KEYFILE"
BOOTH_CONFIG_ACCEPTED_BY_NODE = "BOOTH_CONFIG_ACCEPTED_BY_NODE"
BOOTH_CONFIG_DISTRIBUTION_NODE_ERROR = "BOOTH_CONFIG_DISTRIBUTION_NODE_ERROR"
BOOTH_CONFIG_DISTRIBUTION_STARTED = "BOOTH_CONFIG_DISTRIBUTION_STARTED"
BOOTH_CONFIG_IS_USED = "BOOTH_CONFIG_IS_USED"
BOOTH_CONFIG_READ_ERROR = "BOOTH_CONFIG_READ_ERROR"
BOOTH_CONFIG_UNEXPECTED_LINES = "BOOTH_CONFIG_UNEXPECTED_LINES"
BOOTH_DAEMON_STATUS_ERROR = "BOOTH_DAEMON_STATUS_ERROR"
BOOTH_EVEN_PEERS_NUM = "BOOTH_EVEN_PEERS_NUM"
BOOTH_FETCHING_CONFIG_FROM_NODE = "BOOTH_FETCHING_CONFIG_FROM_NODE"
BOOTH_INVALID_NAME = "BOOTH_INVALID_NAME"
BOOTH_LACK_OF_SITES = "BOOTH_LACK_OF_SITES"
BOOTH_MULTIPLE_TIMES_IN_CIB = "BOOTH_MULTIPLE_TIMES_IN_CIB"
BOOTH_NOT_EXISTS_IN_CIB = "BOOTH_NOT_EXISTS_IN_CIB"
BOOTH_PEERS_STATUS_ERROR = "BOOTH_PEERS_STATUS_ERROR"
BOOTH_SKIPPING_CONFIG = "BOOTH_SKIPPING_CONFIG"
BOOTH_TICKET_DOES_NOT_EXIST = "BOOTH_TICKET_DOES_NOT_EXIST"
BOOTH_TICKET_DUPLICATE = "BOOTH_TICKET_DUPLICATE"
BOOTH_TICKET_NAME_INVALID = "BOOTH_TICKET_NAME_INVALID"
BOOTH_TICKET_OPERATION_FAILED = "BOOTH_TICKET_OPERATION_FAILED"
BOOTH_TICKET_STATUS_ERROR = "BOOTH_TICKET_STATUS_ERROR"
BOOTH_UNSUPPORTED_FILE_LOCATION = "BOOTH_UNSUPPORTED_FILE_LOCATION"
CANNOT_BAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = "CANNOT_BAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
CANNOT_BAN_RESOURCE_STOPPED_NO_NODE_SPECIFIED = "CANNOT_BAN_RESOURCE_STOPPED_NO_NODE_SPECIFIED"
CANNOT_GROUP_RESOURCE_ADJACENT_RESOURCE_FOR_NEW_GROUP = "CANNOT_GROUP_RESOURCE_ADJACENT_RESOURCE_FOR_NEW_GROUP"
CANNOT_GROUP_RESOURCE_ADJACENT_RESOURCE_NOT_IN_GROUP = "CANNOT_GROUP_RESOURCE_ADJACENT_RESOURCE_NOT_IN_GROUP"
CANNOT_GROUP_RESOURCE_ALREADY_IN_THE_GROUP = "CANNOT_GROUP_RESOURCE_ALREADY_IN_THE_GROUP"
CANNOT_GROUP_RESOURCE_MORE_THAN_ONCE = "CANNOT_GROUP_RESOURCE_MORE_THAN_ONCE"
CANNOT_GROUP_RESOURCE_NEXT_TO_ITSELF = "CANNOT_GROUP_RESOURCE_NEXT_TO_ITSELF"
CANNOT_GROUP_RESOURCE_NO_RESOURCES = "CANNOT_GROUP_RESOURCE_NO_RESOURCES"
CANNOT_GROUP_RESOURCE_WRONG_TYPE = "CANNOT_GROUP_RESOURCE_WRONG_TYPE"
CANNOT_MOVE_RESOURCE_BUNDLE = "CANNOT_MOVE_RESOURCE_BUNDLE"
CANNOT_MOVE_RESOURCE_CLONE = "CANNOT_MOVE_RESOURCE_CLONE"
CANNOT_MOVE_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = "CANNOT_MOVE_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
CANNOT_MOVE_RESOURCE_PROMOTABLE_NOT_MASTER = "CANNOT_MOVE_RESOURCE_PROMOTABLE_NOT_MASTER"
CANNOT_MOVE_RESOURCE_STOPPED_NO_NODE_SPECIFIED = "CANNOT_MOVE_RESOURCE_STOPPED_NO_NODE_SPECIFIED"
CANNOT_REMOVE_ALL_CLUSTER_NODES = "CANNOT_REMOVE_ALL_CLUSTER_NODES"
CANNOT_UNMOVE_UNBAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE = "CANNOT_UNMOVE_UNBAN_RESOURCE_MASTER_RESOURCE_NOT_PROMOTABLE"
CIB_ACL_ROLE_IS_ALREADY_ASSIGNED_TO_TARGET = "CIB_ACL_ROLE_IS_ALREADY_ASSIGNED_TO_TARGET"
CIB_ACL_ROLE_IS_NOT_ASSIGNED_TO_TARGET = "CIB_ACL_ROLE_IS_NOT_ASSIGNED_TO_TARGET"
CIB_ACL_TARGET_ALREADY_EXISTS = "CIB_ACL_TARGET_ALREADY_EXISTS"
CIB_ALERT_RECIPIENT_ALREADY_EXISTS = "CIB_ALERT_RECIPIENT_ALREADY_EXISTS"
CIB_ALERT_RECIPIENT_VALUE_INVALID = "CIB_ALERT_RECIPIENT_VALUE_INVALID"
CIB_CANNOT_FIND_MANDATORY_SECTION = "CIB_CANNOT_FIND_MANDATORY_SECTION"
CIB_DIFF_ERROR = "CIB_DIFF_ERROR"
CIB_FENCING_LEVEL_ALREADY_EXISTS = "CIB_FENCING_LEVEL_ALREADY_EXISTS"
CIB_FENCING_LEVEL_DOES_NOT_EXIST = "CIB_FENCING_LEVEL_DOES_NOT_EXIST"
CIB_LOAD_ERROR_BAD_FORMAT = "CIB_LOAD_ERROR_BAD_FORMAT"
CIB_LOAD_ERROR = "CIB_LOAD_ERROR"
CIB_LOAD_ERROR_GET_NODES_FOR_VALIDATION = "CIB_LOAD_ERROR_GET_NODES_FOR_VALIDATION"
CIB_LOAD_ERROR_SCOPE_MISSING = "CIB_LOAD_ERROR_SCOPE_MISSING"
CIB_PUSH_FORCED_FULL_DUE_TO_CRM_FEATURE_SET = "CIB_PUSH_FORCED_FULL_DUE_TO_CRM_FEATURE_SET"
CIB_PUSH_ERROR = "CIB_PUSH_ERROR"
CIB_SAVE_TMP_ERROR = "CIB_SAVE_TMP_ERROR"
CIB_UPGRADE_FAILED = "CIB_UPGRADE_FAILED"
CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION = "CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION"
CIB_UPGRADE_SUCCESSFUL = "CIB_UPGRADE_SUCCESSFUL"
CLUSTER_DESTROY_STARTED = "CLUSTER_DESTROY_STARTED"
CLUSTER_DESTROY_SUCCESS = "CLUSTER_DESTROY_SUCCESS"
CLUSTER_ENABLE_STARTED = "CLUSTER_ENABLE_STARTED"
CLUSTER_ENABLE_SUCCESS = "CLUSTER_ENABLE_SUCCESS"
CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES = "CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES"
CLUSTER_SETUP_SUCCESS = "CLUSTER_SETUP_SUCCESS"
CLUSTER_START_STARTED = "CLUSTER_START_STARTED"
CLUSTER_START_SUCCESS = "CLUSTER_START_SUCCESS"
CLUSTER_WILL_BE_DESTROYED = "CLUSTER_WILL_BE_DESTROYED"
LIVE_ENVIRONMENT_REQUIRED = "LIVE_ENVIRONMENT_REQUIRED"
LIVE_ENVIRONMENT_REQUIRED_FOR_LOCAL_NODE = "LIVE_ENVIRONMENT_REQUIRED_FOR_LOCAL_NODE"
COROSYNC_ADDRESS_IP_VERSION_WRONG_FOR_LINK = "COROSYNC_ADDRESS_IP_VERSION_WRONG_FOR_LINK"
COROSYNC_BAD_NODE_ADDRESSES_COUNT = "COROSYNC_BAD_NODE_ADDRESSES_COUNT"
COROSYNC_CONFIG_ACCEPTED_BY_NODE = "COROSYNC_CONFIG_ACCEPTED_BY_NODE"
COROSYNC_CONFIG_CANNOT_SAVE_INVALID_NAMES_VALUES = "COROSYNC_CONFIG_CANNOT_SAVE_INVALID_NAMES_VALUES"
COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR = "COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR"
COROSYNC_CONFIG_DISTRIBUTION_STARTED = "COROSYNC_CONFIG_DISTRIBUTION_STARTED"
COROSYNC_CONFIG_MISSING_NAMES_OF_NODES = "COROSYNC_CONFIG_MISSING_NAMES_OF_NODES"
COROSYNC_CONFIG_NO_NODES_DEFINED = "COROSYNC_CONFIG_NO_NODES_DEFINED"
COROSYNC_CONFIG_RELOADED = "COROSYNC_CONFIG_RELOADED"
COROSYNC_CONFIG_RELOAD_ERROR = "COROSYNC_CONFIG_RELOAD_ERROR"
COROSYNC_CONFIG_RELOAD_NOT_POSSIBLE = "COROSYNC_CONFIG_RELOAD_NOT_POSSIBLE"
COROSYNC_IP_VERSION_MISMATCH_IN_LINKS = "COROSYNC_IP_VERSION_MISMATCH_IN_LINKS"
COROSYNC_CANNOT_ADD_REMOVE_LINKS_BAD_TRANSPORT = "COROSYNC_CANNOT_ADD_REMOVE_LINKS_BAD_TRANSPORT"
COROSYNC_CANNOT_ADD_REMOVE_LINKS_NO_LINKS_SPECIFIED = "COROSYNC_CANNOT_ADD_REMOVE_LINKS_NO_LINKS_SPECIFIED"
COROSYNC_CANNOT_ADD_REMOVE_LINKS_TOO_MANY_FEW_LINKS = "COROSYNC_CANNOT_ADD_REMOVE_LINKS_TOO_MANY_FEW_LINKS"
COROSYNC_LINK_ALREADY_EXISTS_CANNOT_ADD = "COROSYNC_LINK_ALREADY_EXISTS_CANNOT_ADD"
COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_REMOVE = "COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_REMOVE"
COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_UPDATE = "COROSYNC_LINK_DOES_NOT_EXIST_CANNOT_UPDATE"
COROSYNC_LINK_NUMBER_DUPLICATION = "COROSYNC_LINK_NUMBER_DUPLICATION"
COROSYNC_NODE_ADDRESS_COUNT_MISMATCH = "COROSYNC_NODE_ADDRESS_COUNT_MISMATCH"
COROSYNC_NODE_CONFLICT_CHECK_SKIPPED = "COROSYNC_NODE_CONFLICT_CHECK_SKIPPED"
COROSYNC_NODES_MISSING = "COROSYNC_NODES_MISSING"
COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR = "COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR"
COROSYNC_NOT_RUNNING_CHECK_STARTED = "COROSYNC_NOT_RUNNING_CHECK_STARTED"
COROSYNC_NOT_RUNNING_ON_NODE = "COROSYNC_NOT_RUNNING_ON_NODE"
COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE = "COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE"
COROSYNC_QUORUM_ATB_CANNOT_BE_DISABLED_DUE_TO_SBD = "COROSYNC_QUORUM_ATB_CANNOT_BE_DISABLED_DUE_TO_SBD"
COROSYNC_QUORUM_ATB_WILL_BE_ENABLED_DUE_TO_SBD = "COROSYNC_QUORUM_ATB_WILL_BE_ENABLED_DUE_TO_SBD"
COROSYNC_QUORUM_GET_STATUS_ERROR = "COROSYNC_QUORUM_GET_STATUS_ERROR"
COROSYNC_QUORUM_HEURISTICS_ENABLED_WITH_NO_EXEC = "COROSYNC_QUORUM_HEURISTICS_ENABLED_WITH_NO_EXEC"
COROSYNC_QUORUM_LOSS_UNABLE_TO_CHECK = "COROSYNC_QUORUM_LOSS_UNABLE_TO_CHECK"
COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR = "COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR"
COROSYNC_QUORUM_WILL_BE_LOST = "COROSYNC_QUORUM_WILL_BE_LOST"
COROSYNC_RUNNING_ON_NODE = "COROSYNC_RUNNING_ON_NODE"
COROSYNC_TOO_MANY_LINKS_OPTIONS = "COROSYNC_TOO_MANY_LINKS_OPTIONS"
COROSYNC_TRANSPORT_UNSUPPORTED_OPTIONS = "COROSYNC_TRANSPORT_UNSUPPORTED_OPTIONS"
CRM_MON_ERROR = "CRM_MON_ERROR"
DEFAULTS_CAN_BE_OVERRIDEN = "DEFAULTS_CAN_BE_OVERRIDEN"
DEPRECATED_OPTION = "DEPRECATED_OPTION"
DUPLICATE_CONSTRAINTS_EXIST = "DUPLICATE_CONSTRAINTS_EXIST"
EMPTY_RESOURCE_SET_LIST = "EMPTY_RESOURCE_SET_LIST"
EMPTY_ID = "EMPTY_ID"
FENCE_HISTORY_COMMAND_ERROR = "FENCE_HISTORY_COMMAND_ERROR"
FENCE_HISTORY_NOT_SUPPORTED = "FENCE_HISTORY_NOT_SUPPORTED"
FILES_DISTRIBUTION_SKIPPED = "FILES_DISTRIBUTION_SKIPPED"
FILES_DISTRIBUTION_STARTED = "FILES_DISTRIBUTION_STARTED"
FILES_REMOVE_FROM_NODES_STARTED = "FILES_REMOVE_FROM_NODES_STARTED"
FILES_REMOVE_FROM_NODES_SKIPPED = "FILES_REMOVE_FROM_NODES_SKIPPED"
FILE_ALREADY_EXISTS = "FILE_ALREADY_EXISTS"
FILE_DISTRIBUTION_ERROR = "FILE_DISTRIBUTION_ERROR"
FILE_DISTRIBUTION_SUCCESS = "FILE_DISTRIBUTION_SUCCESS"
FILE_DOES_NOT_EXIST = "FILE_DOES_NOT_EXIST"
FILE_IO_ERROR = "FILE_IO_ERROR"
FILE_REMOVE_FROM_NODE_ERROR = "FILE_REMOVE_FROM_NODE_ERROR"
FILE_REMOVE_FROM_NODE_SUCCESS = "FILE_REMOVE_FROM_NODE_SUCCESS"
HOST_NOT_FOUND = "HOST_NOT_FOUND"
HOST_ALREADY_AUTHORIZED = "HOST_ALREADY_AUTHORIZED"
HOST_ALREADY_IN_CLUSTER_CONFIG = "HOST_ALREADY_IN_CLUSTER_CONFIG"
HOST_ALREADY_IN_CLUSTER_SERVICES = "HOST_ALREADY_IN_CLUSTER_SERVICES"
ID_ALREADY_EXISTS = 'ID_ALREADY_EXISTS'
ID_BELONGS_TO_UNEXPECTED_TYPE = "ID_BELONGS_TO_UNEXPECTED_TYPE"
ID_NOT_FOUND = 'ID_NOT_FOUND'
INVALID_CIB_CONTENT = "INVALID_CIB_CONTENT"
INVALID_ID = "INVALID_ID"
INVALID_OPTIONS = "INVALID_OPTIONS"
INVALID_USERDEFINED_OPTIONS = "INVALID_USERDEFINED_OPTIONS"
INVALID_OPTION_TYPE = "INVALID_OPTION_TYPE"
INVALID_OPTION_VALUE = "INVALID_OPTION_VALUE"
INVALID_RESOURCE_AGENT_NAME = 'INVALID_RESOURCE_AGENT_NAME'
INVALID_RESPONSE_FORMAT = "INVALID_RESPONSE_FORMAT"
INVALID_SCORE = "INVALID_SCORE"
INVALID_STONITH_AGENT_NAME = "INVALID_STONITH_AGENT_NAME"
INVALID_TIMEOUT_VALUE = "INVALID_TIMEOUT_VALUE"
MULTIPLE_SCORE_OPTIONS = "MULTIPLE_SCORE_OPTIONS"
MULTIPLE_RESULTS_FOUND = "MULTIPLE_RESULTS_FOUND"
MUTUALLY_EXCLUSIVE_OPTIONS = "MUTUALLY_EXCLUSIVE_OPTIONS"
NODE_ADDRESSES_ALREADY_EXIST = "NODE_ADDRESSES_ALREADY_EXIST"
NODE_ADDRESSES_CANNOT_BE_EMPTY = "NODE_ADDRESSES_CANNOT_BE_EMPTY"
NODE_ADDRESSES_DUPLICATION = "NODE_ADDRESSES_DUPLICATION"
NODE_ADDRESSES_UNRESOLVABLE = "NODE_ADDRESSES_UNRESOLVABLE"
NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL = "NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL"
NODE_COMMUNICATION_DEBUG_INFO = "NODE_COMMUNICATION_DEBUG_INFO"
NODE_COMMUNICATION_ERROR = "NODE_COMMUNICATION_ERROR"
NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED = "NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED"
NODE_COMMUNICATION_ERROR_PERMISSION_DENIED = "NODE_COMMUNICATION_ERROR_PERMISSION_DENIED"
NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT = "NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT"
NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND = "NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND"
NODE_COMMUNICATION_ERROR_TIMED_OUT = "NODE_COMMUNICATION_ERROR_TIMED_OUT"
NODE_COMMUNICATION_FINISHED = "NODE_COMMUNICATION_FINISHED"
NODE_COMMUNICATION_NOT_CONNECTED = "NODE_COMMUNICATION_NOT_CONNECTED"
NODE_COMMUNICATION_NO_MORE_ADDRESSES = "NODE_COMMUNICATION_NO_MORE_ADDRESSES"
NODE_COMMUNICATION_PROXY_IS_SET = "NODE_COMMUNICATION_PROXY_IS_SET"
NODE_COMMUNICATION_RETRYING = "NODE_COMMUNICATION_RETRYING"
NODE_COMMUNICATION_STARTED = "NODE_COMMUNICATION_STARTED"
NODE_NAMES_ALREADY_EXIST = "NODE_NAMES_ALREADY_EXIST"
NODE_NAMES_DUPLICATION = "NODE_NAMES_DUPLICATION"
NODE_NOT_FOUND = "NODE_NOT_FOUND"
NODE_REMOVE_IN_PACEMAKER_FAILED = "NODE_REMOVE_IN_PACEMAKER_FAILED"
NONE_HOST_FOUND = "NONE_HOST_FOUND"
NODE_USED_AS_TIE_BREAKER = "NODE_USED_AS_TIE_BREAKER"
NODES_TO_REMOVE_UNREACHABLE = "NODES_TO_REMOVE_UNREACHABLE"
NODE_TO_CLEAR_IS_STILL_IN_CLUSTER = "NODE_TO_CLEAR_IS_STILL_IN_CLUSTER"
OMITTING_NODE = "OMITTING_NODE"
OBJECT_WITH_ID_IN_UNEXPECTED_CONTEXT = "OBJECT_WITH_ID_IN_UNEXPECTED_CONTEXT"
PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND = "PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND"
PARSE_ERROR_COROSYNC_CONF = "PARSE_ERROR_COROSYNC_CONF"
PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_AFTER_OPENING_BRACE = "PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_AFTER_OPENING_BRACE"
PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_BEFORE_OR_AFTER_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_EXTRA_CHARACTERS_BEFORE_OR_AFTER_CLOSING_BRACE"
PARSE_ERROR_COROSYNC_CONF_LINE_IS_NOT_SECTION_NOR_KEY_VALUE = "PARSE_ERROR_COROSYNC_CONF_LINE_IS_NOT_SECTION_NOR_KEY_VALUE"
PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE"
PARSE_ERROR_COROSYNC_CONF_MISSING_SECTION_NAME_BEFORE_OPENING_BRACE = "PARSE_ERROR_COROSYNC_CONF_MISSING_SECTION_NAME_BEFORE_OPENING_BRACE"
PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE"
PCSD_VERSION_TOO_OLD = "PCSD_VERSION_TOO_OLD"
PCSD_SSL_CERT_AND_KEY_DISTRIBUTION_STARTED = "PCSD_SSL_CERT_AND_KEY_DISTRIBUTION_STARTED"
PCSD_SSL_CERT_AND_KEY_SET_SUCCESS = "PCSD_SSL_CERT_AND_KEY_SET_SUCCESS"
PREREQUISITE_OPTION_MUST_BE_ENABLED_AS_WELL = "PREREQUISITE_OPTION_MUST_BE_ENABLED_AS_WELL"
PREREQUISITE_OPTION_MUST_BE_DISABLED = "PREREQUISITE_OPTION_MUST_BE_DISABLED"
PREREQUISITE_OPTION_MUST_NOT_BE_SET = "PREREQUISITE_OPTION_MUST_NOT_BE_SET"
PREREQUISITE_OPTION_IS_MISSING = "PREREQUISITE_OPTION_IS_MISSING"
QDEVICE_ALREADY_DEFINED = "QDEVICE_ALREADY_DEFINED"
QDEVICE_ALREADY_INITIALIZED = "QDEVICE_ALREADY_INITIALIZED"
QDEVICE_CERTIFICATE_ACCEPTED_BY_NODE = "QDEVICE_CERTIFICATE_ACCEPTED_BY_NODE"
QDEVICE_CERTIFICATE_DISTRIBUTION_STARTED = "QDEVICE_CERTIFICATE_DISTRIBUTION_STARTED"
QDEVICE_CERTIFICATE_REMOVAL_STARTED = "QDEVICE_CERTIFICATE_REMOVAL_STARTED"
QDEVICE_CERTIFICATE_REMOVED_FROM_NODE = "QDEVICE_CERTIFICATE_REMOVED_FROM_NODE"
QDEVICE_CERTIFICATE_IMPORT_ERROR = "QDEVICE_CERTIFICATE_IMPORT_ERROR"
QDEVICE_CERTIFICATE_SIGN_ERROR = "QDEVICE_CERTIFICATE_SIGN_ERROR"
QDEVICE_DESTROY_ERROR = "QDEVICE_DESTROY_ERROR"
QDEVICE_DESTROY_SUCCESS = "QDEVICE_DESTROY_SUCCESS"
QDEVICE_GET_STATUS_ERROR = "QDEVICE_GET_STATUS_ERROR"
QDEVICE_INITIALIZATION_ERROR = "QDEVICE_INITIALIZATION_ERROR"
QDEVICE_INITIALIZATION_SUCCESS = "QDEVICE_INITIALIZATION_SUCCESS"
QDEVICE_NOT_DEFINED = "QDEVICE_NOT_DEFINED"
QDEVICE_NOT_INITIALIZED = "QDEVICE_NOT_INITIALIZED"
QDEVICE_NOT_RUNNING = "QDEVICE_NOT_RUNNING"
QDEVICE_CLIENT_RELOAD_STARTED = "QDEVICE_CLIENT_RELOAD_STARTED"
QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED = "QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED"
QDEVICE_USED_BY_CLUSTERS = "QDEVICE_USED_BY_CLUSTERS"
REQUIRED_OPTIONS_ARE_MISSING = "REQUIRED_OPTIONS_ARE_MISSING"
REQUIRED_OPTION_OF_ALTERNATIVES_IS_MISSING = "REQUIRED_OPTION_OF_ALTERNATIVES_IS_MISSING"
RESOURCE_BAN_PCMK_ERROR = "RESOURCE_BAN_PCMK_ERROR"
RESOURCE_BAN_PCMK_SUCCESS = "RESOURCE_BAN_PCMK_SUCCESS"
RESOURCE_BUNDLE_ALREADY_CONTAINS_A_RESOURCE = "RESOURCE_BUNDLE_ALREADY_CONTAINS_A_RESOURCE"
RESOURCE_BUNDLE_UNSUPPORTED_CONTAINER_TYPE = "RESOURCE_BUNDLE_UNSUPPORTED_CONTAINER_TYPE"
RESOURCE_CLEANUP_ERROR = "RESOURCE_CLEANUP_ERROR"
RESOURCE_DOES_NOT_RUN = "RESOURCE_DOES_NOT_RUN"
RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE = 'RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE'
RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE = "RESOURCE_IN_BUNDLE_NOT_ACCESSIBLE"
RESOURCE_INSTANCE_ATTR_VALUE_NOT_UNIQUE = "RESOURCE_INSTANCE_ATTR_VALUE_NOT_UNIQUE"
RESOURCE_IS_GUEST_NODE_ALREADY = "RESOURCE_IS_GUEST_NODE_ALREADY"
RESOURCE_IS_UNMANAGED = "RESOURCE_IS_UNMANAGED"
RESOURCE_MANAGED_NO_MONITOR_ENABLED = "RESOURCE_MANAGED_NO_MONITOR_ENABLED"
RESOURCE_MOVE_PCMK_ERROR = "RESOURCE_MOVE_PCMK_ERROR"
RESOURCE_MOVE_PCMK_SUCCESS = "RESOURCE_MOVE_PCMK_SUCCESS"
RESOURCE_OPERATION_INTERVAL_ADAPTED = "RESOURCE_OPERATION_INTERVAL_ADAPTED"
RESOURCE_OPERATION_INTERVAL_DUPLICATION = "RESOURCE_OPERATION_INTERVAL_DUPLICATION"
RESOURCE_REFRESH_ERROR = "RESOURCE_REFRESH_ERROR"
RESOURCE_REFRESH_TOO_TIME_CONSUMING = 'RESOURCE_REFRESH_TOO_TIME_CONSUMING'
RESOURCE_RUNNING_ON_NODES = "RESOURCE_RUNNING_ON_NODES"
RESOURCE_UNMOVE_UNBAN_PCMK_ERROR = "RESOURCE_UNMOVE_UNBAN_PCMK_ERROR"
RESOURCE_UNMOVE_UNBAN_PCMK_SUCCESS = "RESOURCE_UNMOVE_UNBAN_PCMK_SUCCESS"
RESOURCE_UNMOVE_UNBAN_PCMK_EXPIRED_NOT_SUPPORTED = "RESOURCE_UNMOVE_UNBAN_PCMK_EXPIRED_NOT_SUPPORTED"
RUN_EXTERNAL_PROCESS_ERROR = "RUN_EXTERNAL_PROCESS_ERROR"
RUN_EXTERNAL_PROCESS_FINISHED = "RUN_EXTERNAL_PROCESS_FINISHED"
RUN_EXTERNAL_PROCESS_STARTED = "RUN_EXTERNAL_PROCESS_STARTED"
SBD_CHECK_STARTED = "SBD_CHECK_STARTED"
SBD_CHECK_SUCCESS = "SBD_CHECK_SUCCESS"
SBD_CONFIG_ACCEPTED_BY_NODE = "SBD_CONFIG_ACCEPTED_BY_NODE"
SBD_CONFIG_DISTRIBUTION_STARTED = "SBD_CONFIG_DISTRIBUTION_STARTED"
SBD_DEVICE_DOES_NOT_EXIST = "SBD_DEVICE_DOES_NOT_EXIST"
SBD_DEVICE_DUMP_ERROR = "SBD_DEVICE_DUMP_ERROR"
SBD_DEVICE_INITIALIZATION_ERROR = "SBD_DEVICE_INITIALIZATION_ERROR"
SBD_DEVICE_INITIALIZATION_STARTED = "SBD_DEVICE_INITIALIZATION_STARTED"
SBD_DEVICE_INITIALIZATION_SUCCESS = "SBD_DEVICE_INITIALIZATION_SUCCESS"
SBD_DEVICE_IS_NOT_BLOCK_DEVICE = "SBD_DEVICE_IS_NOT_BLOCK_DEVICE"
SBD_DEVICE_LIST_ERROR = "SBD_DEVICE_LIST_ERROR"
SBD_DEVICE_MESSAGE_ERROR = "SBD_DEVICE_MESSAGE_ERROR"
SBD_DEVICE_PATH_NOT_ABSOLUTE = "SBD_DEVICE_PATH_NOT_ABSOLUTE"
SBD_DISABLING_STARTED = "SBD_DISABLING_STARTED"
SBD_ENABLING_STARTED = "SBD_ENABLING_STARTED"
SBD_LIST_WATCHDOG_ERROR = "SBD_LIST_WATCHDOG_ERROR"
SBD_NO_DEVICE_FOR_NODE = "SBD_NO_DEVICE_FOR_NODE"
SBD_NOT_INSTALLED = "SBD_NOT_INSTALLED"
SBD_NOT_USED_CANNOT_SET_SBD_OPTIONS = "SBD_NOT_USED_CANNOT_SET_SBD_OPTIONS"
SBD_TOO_MANY_DEVICES_FOR_NODE = "SBD_TOO_MANY_DEVICES_FOR_NODE"
SBD_WITH_DEVICES_NOT_USED_CANNOT_SET_DEVICE = "SBD_WITH_DEVICES_NOT_USED_CANNOT_SET_DEVICE"
SBD_WATCHDOG_NOT_SUPPORTED = "SBD_WATCHDOG_NOT_SUPPORTED"
SBD_WATCHDOG_VALIDATION_INACTIVE = "SBD_WATCHDOG_VALIDATION_INACTIVE"
SBD_WATCHDOG_TEST_ERROR = "SBD_WATCHDOG_TEST_ERROR"
SBD_WATCHDOG_TEST_MULTUPLE_DEVICES = "SBD_WATCHDOG_TEST_MULTUPLE_DEVICES"
SBD_WATCHDOG_TEST_FAILED = "SBD_WATCHDOG_TEST_FAILED"
SERVICE_DISABLE_ERROR = "SERVICE_DISABLE_ERROR"
SERVICE_DISABLE_STARTED = "SERVICE_DISABLE_STARTED"
SERVICE_DISABLE_SUCCESS = "SERVICE_DISABLE_SUCCESS"
SERVICE_ENABLE_ERROR = "SERVICE_ENABLE_ERROR"
SERVICE_ENABLE_STARTED = "SERVICE_ENABLE_STARTED"
SERVICE_ENABLE_SKIPPED = "SERVICE_ENABLE_SKIPPED"
SERVICE_ENABLE_SUCCESS = "SERVICE_ENABLE_SUCCESS"
SERVICE_KILL_ERROR = "SERVICE_KILL_ERROR"
SERVICE_KILL_SUCCESS = "SERVICE_KILL_SUCCESS"
SERVICE_NOT_INSTALLED = "SERVICE_NOT_INSTALLED"
SERVICE_START_ERROR = "SERVICE_START_ERROR"
SERVICE_START_SKIPPED = "SERVICE_START_SKIPPED"
SERVICE_START_STARTED = "SERVICE_START_STARTED"
SERVICE_START_SUCCESS = "SERVICE_START_SUCCESS"
SERVICE_STOP_ERROR = "SERVICE_STOP_ERROR"
SERVICE_STOP_STARTED = "SERVICE_STOP_STARTED"
SERVICE_STOP_SUCCESS = "SERVICE_STOP_SUCCESS"
SERVICE_VERSION_MISMATCH = "SERVICE_VERSION_MISMATCH"
STONITH_RESOURCES_DO_NOT_EXIST = "STONITH_RESOURCES_DO_NOT_EXIST"
SERVICE_COMMANDS_ON_NODES_STARTED = "SERVICE_COMMANDS_ON_NODES_STARTED"
SERVICE_COMMANDS_ON_NODES_SKIPPED = "SERVICE_COMMANDS_ON_NODES_SKIPPED"
SERVICE_COMMAND_ON_NODE_ERROR = "SERVICE_COMMAND_ON_NODE_ERROR"
SERVICE_COMMAND_ON_NODE_SUCCESS = "SERVICE_COMMAND_ON_NODE_SUCCESS"
SYSTEM_WILL_RESET = "SYSTEM_WILL_RESET"
TMP_FILE_WRITE = "TMP_FILE_WRITE"
UNABLE_TO_CONNECT_TO_ANY_REMAINING_NODE = "UNABLE_TO_CONNECT_TO_ANY_REMAINING_NODE"
UNABLE_TO_CONNECT_TO_ALL_REMAINING_NODE = "UNABLE_TO_CONNECT_TO_ALL_REMAINING_NODE"
UNABLE_TO_DETERMINE_USER_UID = "UNABLE_TO_DETERMINE_USER_UID"
UNABLE_TO_DETERMINE_GROUP_GID = "UNABLE_TO_DETERMINE_GROUP_GID"
UNABLE_TO_GET_AGENT_METADATA = 'UNABLE_TO_GET_AGENT_METADATA'
UNABLE_TO_READ_COROSYNC_CONFIG = "UNABLE_TO_READ_COROSYNC_CONFIG"
UNABLE_TO_GET_SBD_CONFIG = "UNABLE_TO_GET_SBD_CONFIG"
UNABLE_TO_GET_SBD_STATUS = "UNABLE_TO_GET_SBD_STATUS"
UNABLE_TO_PERFORM_OPERATION_ON_ANY_NODE = "UNABLE_TO_PERFORM_OPERATION_ON_ANY_NODE"
WATCHDOG_INVALID = "WATCHDOG_INVALID"
UNSUPPORTED_OPERATION_ON_NON_SYSTEMD_SYSTEMS = "UNSUPPORTED_OPERATION_ON_NON_SYSTEMD_SYSTEMS"
USE_COMMAND_NODE_ADD_REMOTE = "USE_COMMAND_NODE_ADD_REMOTE"
USE_COMMAND_NODE_ADD_GUEST = "USE_COMMAND_NODE_ADD_GUEST"
USE_COMMAND_NODE_REMOVE_GUEST = "USE_COMMAND_NODE_REMOVE_GUEST"
USING_KNOWN_HOST_ADDRESS_FOR_HOST = "USING_KNOWN_HOST_ADDRESS_FOR_HOST"
USING_DEFAULT_WATCHDOG = "USING_DEFAULT_WATCHDOG"
WAIT_FOR_IDLE_ERROR = "WAIT_FOR_IDLE_ERROR"
WAIT_FOR_IDLE_NOT_LIVE_CLUSTER = "WAIT_FOR_IDLE_NOT_LIVE_CLUSTER"
WAIT_FOR_IDLE_NOT_SUPPORTED = "WAIT_FOR_IDLE_NOT_SUPPORTED"
WAIT_FOR_IDLE_TIMED_OUT = "WAIT_FOR_IDLE_TIMED_OUT"
WAIT_FOR_NODE_STARTUP_ERROR = "WAIT_FOR_NODE_STARTUP_ERROR"
WAIT_FOR_NODE_STARTUP_STARTED = "WAIT_FOR_NODE_STARTUP_STARTED"
WAIT_FOR_NODE_STARTUP_TIMED_OUT = "WAIT_FOR_NODE_STARTUP_TIMED_OUT"
WAIT_FOR_NODE_STARTUP_WITHOUT_START = "WAIT_FOR_NODE_STARTUP_WITHOUT_START"
WATCHDOG_NOT_FOUND = "WATCHDOG_NOT_FOUND"
