from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

# force cathegories
FORCE_ACTIVE_RRP = "ACTIVE_RRP"
FORCE_ALERT_RECIPIENT_VALUE_NOT_UNIQUE = "FORCE_ALERT_RECIPIENT_VALUE_NOT_UNIQUE"
FORCE_BOOTH_REMOVE_FROM_CIB = "FORCE_BOOTH_REMOVE_FROM_CIB"
FORCE_FILE_OVERWRITE = "FORCE_FILE_OVERWRITE"
FORCE_CONSTRAINT_DUPLICATE = "CONSTRAINT_DUPLICATE"
FORCE_CONSTRAINT_MULTIINSTANCE_RESOURCE = "CONSTRAINT_MULTIINSTANCE_RESOURCE"
FORCE_LOAD_THRESHOLD = "LOAD_THRESHOLD"
FORCE_OPTIONS = "OPTIONS"
FORCE_QDEVICE_MODEL = "QDEVICE_MODEL"
FORCE_UNKNOWN_AGENT = "UNKNOWN_AGENT"
FORCE_UNSUPPORTED_AGENT = "UNSUPPORTED_AGENT"
FORCE_METADATA_ISSUE = "METADATA_ISSUE"
SKIP_OFFLINE_NODES = "SKIP_OFFLINE_NODES"

AGENT_GENERAL_ERROR = "AGENT_GENERAL_ERROR"
AGENT_NOT_FOUND = "AGENT_NOT_FOUND"
BAD_CLUSTER_STATE_FORMAT = 'BAD_CLUSTER_STATE_FORMAT'
BOOTH_ADDRESS_DUPLICATION = "BOOTH_ADDRESS_DUPLICATION"
BOOTH_ALREADY_CREATED = "BOOTH_ALREADY_CREATED"
BOOTH_CONFIG_INVALID_CONTENT = "BOOTH_CONFIG_INVALID_CONTENT"
BOOTH_CONFIG_UNEXPECTED_LINES = "BOOTH_CONFIG_UNEXPECTED_LINES"
BOOTH_EVEN_PARTICIPANTS_NUM = "BOOTH_EVEN_PARTICIPANTS_NUM"
BOOTH_INVALID_NAME = "BOOTH_INVALID_NAME"
BOOTH_LACK_OF_SITES = "BOOTH_LACK_OF_SITES"
BOOTH_MULTIPLE_TIMES_IN_CIB = "BOOTH_MULTIPLE_TIMES_IN_CIB"
BOOTH_NOT_EXISTS_IN_CIB = "BOOTH_NOT_EXISTS_IN_CIB"
BOOTH_TICKET_DOES_NOT_EXIST = "BOOTH_TICKET_DOES_NOT_EXIST"
BOOTH_TICKET_DUPLICATE = "BOOTH_TICKET_DUPLICATE"
BOOTH_TICKET_NAME_INVALID = "BOOTH_TICKET_NAME_INVALID"
CIB_ALERT_NOT_FOUND = "CIB_ALERT_NOT_FOUND"
CIB_ALERT_RECIPIENT_ALREADY_EXISTS = "CIB_ALERT_RECIPIENT_ALREADY_EXISTS"
CIB_ALERT_RECIPIENT_VALUE_INVALID = "CIB_ALERT_RECIPIENT_VALUE_INVALID"
CIB_CANNOT_FIND_MANDATORY_SECTION = "CIB_CANNOT_FIND_MANDATORY_SECTION"
CIB_LOAD_ERROR_BAD_FORMAT = "CIB_LOAD_ERROR_BAD_FORMAT"
CIB_LOAD_ERROR = "CIB_LOAD_ERROR"
CIB_LOAD_ERROR_SCOPE_MISSING = "CIB_LOAD_ERROR_SCOPE_MISSING"
CIB_PUSH_ERROR = "CIB_PUSH_ERROR"
CIB_UPGRADE_FAILED = "CIB_UPGRADE_FAILED"
CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION = "CIB_UPGRADE_FAILED_TO_MINIMAL_REQUIRED_VERSION"
CIB_UPGRADE_SUCCESSFUL = "CIB_UPGRADE_SUCCESSFUL"
CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES = "CLUSTER_RESTART_REQUIRED_TO_APPLY_CHANGES"
CMAN_BROADCAST_ALL_RINGS = 'CMAN_BROADCAST_ALL_RINGS'
CMAN_UDPU_RESTART_REQUIRED = 'CMAN_UDPU_RESTART_REQUIRED'
CMAN_UNSUPPORTED_COMMAND = "CMAN_UNSUPPORTED_COMMAND"
COMMON_ERROR = 'COMMON_ERROR'
COMMON_INFO = 'COMMON_INFO'
COROSYNC_CONFIG_ACCEPTED_BY_NODE = "COROSYNC_CONFIG_ACCEPTED_BY_NODE"
COROSYNC_CONFIG_DISTRIBUTION_STARTED = "COROSYNC_CONFIG_DISTRIBUTION_STARTED"
COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR = "COROSYNC_CONFIG_DISTRIBUTION_NODE_ERROR"
COROSYNC_CONFIG_RELOADED = "COROSYNC_CONFIG_RELOADED"
COROSYNC_CONFIG_RELOAD_ERROR = "COROSYNC_CONFIG_RELOAD_ERROR"
COROSYNC_NOT_RUNNING_CHECK_STARTED = "COROSYNC_NOT_RUNNING_CHECK_STARTED"
COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR = "COROSYNC_NOT_RUNNING_CHECK_NODE_ERROR"
COROSYNC_NOT_RUNNING_ON_NODE = "COROSYNC_NOT_RUNNING_ON_NODE"
COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE = "COROSYNC_OPTIONS_INCOMPATIBLE_WITH_QDEVICE"
COROSYNC_QUORUM_GET_STATUS_ERROR = "COROSYNC_QUORUM_GET_STATUS_ERROR"
COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR = "COROSYNC_QUORUM_SET_EXPECTED_VOTES_ERROR"
COROSYNC_RUNNING_ON_NODE = "COROSYNC_RUNNING_ON_NODE"
CRM_MON_ERROR = "CRM_MON_ERROR"
DUPLICATE_CONSTRAINTS_EXIST = "DUPLICATE_CONSTRAINTS_EXIST"
EMPTY_RESOURCE_SET_LIST = "EMPTY_RESOURCE_SET_LIST"
FILE_ALREADY_EXISTS = "FILE_ALREADY_EXISTS"
FILE_DOES_NOT_EXIST = "FILE_DOES_NOT_EXIST"
FILE_IO_ERROR = "FILE_IO_ERROR"
ID_ALREADY_EXISTS = 'ID_ALREADY_EXISTS'
ID_NOT_FOUND = 'ID_NOT_FOUND'
IGNORED_CMAN_UNSUPPORTED_OPTION = 'IGNORED_CMAN_UNSUPPORTED_OPTION'
INVALID_ID = "INVALID_ID"
INVALID_METADATA_FORMAT = 'INVALID_METADATA_FORMAT'
INVALID_OPTION = "INVALID_OPTION"
INVALID_OPTION_VALUE = "INVALID_OPTION_VALUE"
INVALID_RESOURCE_NAME = 'INVALID_RESOURCE_NAME'
INVALID_RESPONSE_FORMAT = "INVALID_RESPONSE_FORMAT"
INVALID_SCORE = "INVALID_SCORE"
INVALID_TIMEOUT_VALUE = "INVALID_TIMEOUT_VALUE"
MULTIPLE_SCORE_OPTIONS = "MULTIPLE_SCORE_OPTIONS"
NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL = "NODE_COMMUNICATION_COMMAND_UNSUCCESSFUL"
NODE_COMMUNICATION_ERROR = "NODE_COMMUNICATION_ERROR"
NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED = "NODE_COMMUNICATION_ERROR_NOT_AUTHORIZED"
NODE_COMMUNICATION_ERROR_PERMISSION_DENIED = "NODE_COMMUNICATION_ERROR_PERMISSION_DENIED"
NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT = "NODE_COMMUNICATION_ERROR_UNABLE_TO_CONNECT"
NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND = "NODE_COMMUNICATION_ERROR_UNSUPPORTED_COMMAND"
NODE_COMMUNICATION_FINISHED = "NODE_COMMUNICATION_FINISHED"
NODE_COMMUNICATION_NOT_CONNECTED = "NODE_COMMUNICATION_NOT_CONNECTED"
NODE_COMMUNICATION_STARTED = "NODE_COMMUNICATION_STARTED"
NODE_NOT_FOUND = "NODE_NOT_FOUND"
NON_UDP_TRANSPORT_ADDR_MISMATCH = 'NON_UDP_TRANSPORT_ADDR_MISMATCH'
OMITTING_NODE = "OMITTING_NODE"
PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND = "PACEMAKER_LOCAL_NODE_NAME_NOT_FOUND"
PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_MISSING_CLOSING_BRACE"
PARSE_ERROR_COROSYNC_CONF = "PARSE_ERROR_COROSYNC_CONF"
PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE = "PARSE_ERROR_COROSYNC_CONF_UNEXPECTED_CLOSING_BRACE"
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
QDEVICE_CLIENT_RELOAD_STARTED = "QDEVICE_CLIENT_RELOAD_STARTED"
QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED = "QDEVICE_REMOVE_OR_CLUSTER_STOP_NEEDED"
REQUIRED_OPTION_IS_MISSING = "REQUIRED_OPTION_IS_MISSING"
RESOURCE_CLEANUP_ERROR = "RESOURCE_CLEANUP_ERROR"
RESOURCE_CLEANUP_TOO_TIME_CONSUMING = 'RESOURCE_CLEANUP_TOO_TIME_CONSUMING'
RESOURCE_DOES_NOT_EXIST = 'RESOURCE_DOES_NOT_EXIST'
RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE = 'RESOURCE_FOR_CONSTRAINT_IS_MULTIINSTANCE'
RESOURCE_WAIT_ERROR = "RESOURCE_WAIT_ERROR"
RESOURCE_WAIT_NOT_SUPPORTED = "RESOURCE_WAIT_NOT_SUPPORTED"
RESOURCE_WAIT_TIMED_OUT = "RESOURCE_WAIT_TIMED_OUT"
RRP_ACTIVE_NOT_SUPPORTED = 'RRP_ACTIVE_NOT_SUPPORTED'
RUN_EXTERNAL_PROCESS_ERROR = "RUN_EXTERNAL_PROCESS_ERROR"
RUN_EXTERNAL_PROCESS_FINISHED = "RUN_EXTERNAL_PROCESS_FINISHED"
RUN_EXTERNAL_PROCESS_STARTED = "RUN_EXTERNAL_PROCESS_STARTED"
SBD_CHECK_STARTED = "SBD_CHECK_STARTED"
SBD_CHECK_SUCCESS = "SBD_CHECK_SUCCESS"
SBD_CONFIG_DISTRIBUTION_STARTED = "SBD_CONFIG_DISTRIBUTION_STARTED"
SBD_CONFIG_ACCEPTED_BY_NODE = "SBD_CONFIG_ACCEPTED_BY_NODE"
SBD_DISABLING_STARTED = "SBD_DISABLING_STARTED"
SBD_ENABLING_STARTED = "SBD_ENABLING_STARTED"
SBD_NOT_INSTALLED = "SBD_NOT_INSTALLED"
SBD_NOT_ENABLED = "SBD_NOT_ENABLED"
SERVICE_DISABLE_ERROR = "SERVICE_DISABLE_ERROR"
SERVICE_DISABLE_STARTED = "SERVICE_DISABLE_STARTED"
SERVICE_DISABLE_SUCCESS = "SERVICE_DISABLE_SUCCESS"
SERVICE_ENABLE_ERROR = "SERVICE_ENABLE_ERROR"
SERVICE_ENABLE_STARTED = "SERVICE_ENABLE_STARTED"
SERVICE_ENABLE_SKIPPED = "SERVICE_ENABLE_SKIPPED"
SERVICE_ENABLE_SUCCESS = "SERVICE_ENABLE_SUCCESS"
SERVICE_KILL_ERROR = "SERVICE_KILL_ERROR"
SERVICE_KILL_SUCCESS = "SERVICE_KILL_SUCCESS"
SERVICE_START_ERROR = "SERVICE_START_ERROR"
SERVICE_START_SKIPPED = "SERVICE_START_SKIPPED"
SERVICE_START_STARTED = "SERVICE_START_STARTED"
SERVICE_START_SUCCESS = "SERVICE_START_SUCCESS"
SERVICE_STOP_ERROR = "SERVICE_STOP_ERROR"
SERVICE_STOP_STARTED = "SERVICE_STOP_STARTED"
SERVICE_STOP_SUCCESS = "SERVICE_STOP_SUCCESS"
UNABLE_TO_GET_AGENT_METADATA = 'UNABLE_TO_GET_AGENT_METADATA'
UNABLE_TO_READ_COROSYNC_CONFIG = "UNABLE_TO_READ_COROSYNC_CONFIG"
UNABLE_TO_GET_SBD_CONFIG = "UNABLE_TO_GET_SBD_CONFIG"
UNABLE_TO_GET_SBD_STATUS = "UNABLE_TO_GET_SBD_STATUS"
UNKNOWN_COMMAND = 'UNKNOWN_COMMAND'
UNSUPPORTED_AGENT = 'UNSUPPORTED_AGENT'
WATCHDOG_NOT_FOUND = "WATCHDOG_NOT_FOUND"
