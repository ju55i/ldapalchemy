import ctypes


LDAP_VERSION1 = ctypes.c_int(1)
LDAP_VERSION2 = ctypes.c_int(2)
LDAP_VERSION3 = ctypes.c_int(3)
LDAP_VERSION_MIN = LDAP_VERSION2
LDAP_VERSION = LDAP_VERSION2
LDAP_VERSION_MAX = LDAP_VERSION3

#  We use 3000+n here because it is above 1823 (for RFC 1823),
#  above 2000+rev of IETF LDAPEXT draft (now quite dated),
#  yet below allocations for new RFCs (just in case there is
#  someday an RFC produced).
LDAP_API_VERSION = ctypes.c_int(3001)
LDAP_VENDOR_NAME = "OpenLDAP"

# OpenLDAP API Features
#LDAP_API_FEATURE_X_OPENLDAP = LDAP_VENDOR_VERSION
LDAP_PORT = ctypes.c_int(389)  # ldap:///		default LDAP port
LDAPS_PORT = ctypes.c_int(636)  # ldaps:///	default LDAP over TLS port
LDAP_ROOT_DSE = ""
LDAP_NO_ATTRS = "1.1"
LDAP_ALL_USER_ATTRIBUTES = "*"
LDAP_ALL_OPERATIONAL_ATTRIBUTES = "+"  # RFC 3673

# RFC 4511:  maxInt INTEGER ::= 2147483647 -- (2^^31 - 1) --
LDAP_MAXINT = ctypes.c_int(2147483647)

#  LDAP_OPTions
# 	0x0000 - 0x0fff reserved for api options
# 	0x1000 - 0x3fff reserved for api extended options
# 	0x4000 - 0x7fff reserved for private and experimental options
LDAP_OPT_API_INFO = ctypes.c_int(0x0000)
LDAP_OPT_DESC = ctypes.c_int(0x0001)  # historic
LDAP_OPT_DEREF = ctypes.c_int(0x0002)
LDAP_OPT_SIZELIMIT = ctypes.c_int(0x0003)
LDAP_OPT_TIMELIMIT = ctypes.c_int(0x0004)

# 0x05 - 0x07 not defined
LDAP_OPT_REFERRALS = ctypes.c_int(0x0008)
LDAP_OPT_RESTART = ctypes.c_int(0x0009)

# 0x0a - 0x10 not defined
LDAP_OPT_PROTOCOL_VERSION = ctypes.c_int(0x0011)
LDAP_OPT_SERVER_CONTROLS = ctypes.c_int(0x0012)
LDAP_OPT_CLIENT_CONTROLS = ctypes.c_int(0x0013)

# 0x14 not defined
LDAP_OPT_API_FEATURE_INFO = ctypes.c_int(0x0015)

# 0x16 - 0x2f not defined
LDAP_OPT_HOST_NAME = ctypes.c_int(0x0030)
LDAP_OPT_RESULT_CODE = ctypes.c_int(0x0031)
LDAP_OPT_ERROR_NUMBER = LDAP_OPT_RESULT_CODE
LDAP_OPT_DIAGNOSTIC_MESSAGE = ctypes.c_int(0x0032)
LDAP_OPT_ERROR_STRING = LDAP_OPT_DIAGNOSTIC_MESSAGE
LDAP_OPT_MATCHED_DN = ctypes.c_int(0x0033)

# 0x0034 - 0x3fff not defined
# 0x0091 used by Microsoft for LDAP_OPT_AUTO_RECONNECT
LDAP_OPT_SSPI_FLAGS = ctypes.c_int(0x0092)

# 0x0093 used by Microsoft for LDAP_OPT_SSL_INFO
# 0x0094 used by Microsoft for LDAP_OPT_REF_DEREF_CONN_PER_MSG
LDAP_OPT_SIGN = ctypes.c_int(0x0095)
LDAP_OPT_ENCRYPT = ctypes.c_int(0x0096)
LDAP_OPT_SASL_METHOD = ctypes.c_int(0x0097)

# 0x0098 used by Microsoft for LDAP_OPT_AREC_EXCLUSIVE
LDAP_OPT_SECURITY_CONTEXT = ctypes.c_int(0x0099)

# 0x009A used by Microsoft for LDAP_OPT_ROOTDSE_CACHE
# 0x009B - 0x3fff not defined
# API Extensions
LDAP_OPT_API_EXTENSION_BASE = ctypes.c_int(0x4000)  # API extensions

# private and experimental options
# OpenLDAP specific options
LDAP_OPT_DEBUG_LEVEL = ctypes.c_int(0x5001)  # debug level
LDAP_OPT_TIMEOUT = ctypes.c_int(0x5002)  # default timeout
LDAP_OPT_REFHOPLIMIT = ctypes.c_int(0x5003)  # ref hop limit
LDAP_OPT_NETWORK_TIMEOUT = ctypes.c_int(0x5005)  # socket level timeout
LDAP_OPT_URI = ctypes.c_int(0x5006)
LDAP_OPT_REFERRAL_URLS = ctypes.c_int(0x5007)  # Referral URLs
LDAP_OPT_SOCKBUF = ctypes.c_int(0x5008)  # sockbuf
LDAP_OPT_DEFBASE = ctypes.c_int(0x5009)  # searchbase
LDAP_OPT_CONNECT_ASYNC = ctypes.c_int(0x5010)  # create connections asynchronously
LDAP_OPT_CONNECT_CB = ctypes.c_int(0x5011)  # connection callbacks
LDAP_OPT_SESSION_REFCNT = ctypes.c_int(0x5012)  # session reference count

# OpenLDAP TLS options
LDAP_OPT_X_TLS = ctypes.c_int(0x6000)
LDAP_OPT_X_TLS_CTX = ctypes.c_int(0x6001)  # OpenSSL CTX*
LDAP_OPT_X_TLS_CACERTFILE = ctypes.c_int(0x6002)
LDAP_OPT_X_TLS_CACERTDIR = ctypes.c_int(0x6003)
LDAP_OPT_X_TLS_CERTFILE = ctypes.c_int(0x6004)
LDAP_OPT_X_TLS_KEYFILE = ctypes.c_int(0x6005)
LDAP_OPT_X_TLS_REQUIRE_CERT = ctypes.c_int(0x6006)
LDAP_OPT_X_TLS_PROTOCOL_MIN = ctypes.c_int(0x6007)
LDAP_OPT_X_TLS_CIPHER_SUITE = ctypes.c_int(0x6008)
LDAP_OPT_X_TLS_RANDOM_FILE = ctypes.c_int(0x6009)
LDAP_OPT_X_TLS_SSL_CTX = ctypes.c_int(0x600a)  # OpenSSL SSL*
LDAP_OPT_X_TLS_CRLCHECK = ctypes.c_int(0x600b)
LDAP_OPT_X_TLS_CONNECT_CB = ctypes.c_int(0x600c)
LDAP_OPT_X_TLS_CONNECT_ARG = ctypes.c_int(0x600d)
LDAP_OPT_X_TLS_DHFILE = ctypes.c_int(0x600e)
LDAP_OPT_X_TLS_NEWCTX = ctypes.c_int(0x600f)
LDAP_OPT_X_TLS_CRLFILE = ctypes.c_int(0x6010)  # GNUtls only
LDAP_OPT_X_TLS_PACKAGE = ctypes.c_int(0x6011)
LDAP_OPT_X_TLS_NEVER = ctypes.c_int(0)
LDAP_OPT_X_TLS_HARD = ctypes.c_int(1)
LDAP_OPT_X_TLS_DEMAND = ctypes.c_int(2)
LDAP_OPT_X_TLS_ALLOW = ctypes.c_int(3)
LDAP_OPT_X_TLS_TRY = ctypes.c_int(4)
LDAP_OPT_X_TLS_CRL_NONE = ctypes.c_int(0)
LDAP_OPT_X_TLS_CRL_PEER = ctypes.c_int(1)
LDAP_OPT_X_TLS_CRL_ALL = ctypes.c_int(2)

# OpenLDAP SASL options
LDAP_OPT_X_SASL_MECH = ctypes.c_int(0x6100)
LDAP_OPT_X_SASL_REALM = ctypes.c_int(0x6101)
LDAP_OPT_X_SASL_AUTHCID = ctypes.c_int(0x6102)
LDAP_OPT_X_SASL_AUTHZID = ctypes.c_int(0x6103)
LDAP_OPT_X_SASL_SSF = ctypes.c_int(0x6104)  # read-only
LDAP_OPT_X_SASL_SSF_EXTERNAL = ctypes.c_int(0x6105)  # write-only
LDAP_OPT_X_SASL_SECPROPS = ctypes.c_int(0x6106)  # write-only
LDAP_OPT_X_SASL_SSF_MIN = ctypes.c_int(0x6107)
LDAP_OPT_X_SASL_SSF_MAX = ctypes.c_int(0x6108)
LDAP_OPT_X_SASL_MAXBUFSIZE = ctypes.c_int(0x6109)
LDAP_OPT_X_SASL_MECHLIST = ctypes.c_int(0x610a)  # read-only
LDAP_OPT_X_SASL_NOCANON = ctypes.c_int(0x610b)
LDAP_OPT_X_SASL_USERNAME = ctypes.c_int(0x610c)  # read-only
LDAP_OPT_X_SASL_GSS_CREDS = ctypes.c_int(0x610d)

# OpenLDAP GSSAPI options
LDAP_OPT_X_GSSAPI_DO_NOT_FREE_CONTEXT = ctypes.c_int(0x6200)
LDAP_OPT_X_GSSAPI_ALLOW_REMOTE_PRINCIPAL = ctypes.c_int(0x6201)

#  OpenLDAP per connection tcp-keepalive settings
#  (Linux only, ignored where unsupported)
LDAP_OPT_X_KEEPALIVE_IDLE = ctypes.c_int(0x6300)
LDAP_OPT_X_KEEPALIVE_PROBES = ctypes.c_int(0x6301)
LDAP_OPT_X_KEEPALIVE_INTERVAL = ctypes.c_int(0x6302)

# Private API Extensions -- reserved for application use
LDAP_OPT_PRIVATE_EXTENSION_BASE = ctypes.c_int(0x7000)  # Private API inclusive

#  ldap_get_option() and ldap_set_option() return values.
#  As later versions may return other values indicating
#  failure, current applications should only compare returned
#  value against LDAP_OPT_SUCCESS.
LDAP_OPT_SUCCESS = ctypes.c_int(0)
LDAP_OPT_ERROR = ctypes.c_int(-1)
LDAP_API_INFO_VERSION = ctypes.c_int(1)
LDAP_FEATURE_INFO_VERSION = ctypes.c_int(1)  # apifeature_info struct version

# LDAP Controls
# standard track controls
LDAP_CONTROL_MANAGEDSAIT = "2.16.840.1.113730.3.4.2"  # RFC 3296
LDAP_CONTROL_PROXY_AUTHZ = "2.16.840.1.113730.3.4.18"  # RFC 4370
LDAP_CONTROL_SUBENTRIES = "1.3.6.1.4.1.4203.1.10.1"  # RFC 3672
LDAP_CONTROL_VALUESRETURNFILTER = "1.2.826.0.1.3344810.2.3"  # RFC 3876
LDAP_CONTROL_ASSERT = "1.3.6.1.1.12"  # RFC 4528
LDAP_CONTROL_PRE_READ = "1.3.6.1.1.13.1"  # RFC 4527
LDAP_CONTROL_POST_READ = "1.3.6.1.1.13.2"  # RFC 4527
LDAP_CONTROL_SORTREQUEST = "1.2.840.113556.1.4.473"  # RFC 2891
LDAP_CONTROL_SORTRESPONSE = "1.2.840.113556.1.4.474"  # RFC 2891

# non-standard track controls
LDAP_CONTROL_PAGEDRESULTS = "1.2.840.113556.1.4.319"  # RFC 2696

# LDAP Content Synchronization Operation -- RFC 4533
LDAP_SYNC_OID = "1.3.6.1.4.1.4203.1.9.1"
LDAP_CONTROL_SYNC = LDAP_SYNC_OID + ".1"
LDAP_CONTROL_SYNC_STATE = LDAP_SYNC_OID + ".2"
LDAP_CONTROL_SYNC_DONE = LDAP_SYNC_OID + ".3"
LDAP_SYNC_INFO = LDAP_SYNC_OID + ".4"
LDAP_SYNC_NONE = ctypes.c_int(0x00)
LDAP_SYNC_REFRESH_ONLY = ctypes.c_int(0x01)
LDAP_SYNC_RESERVED = ctypes.c_int(0x02)
LDAP_SYNC_REFRESH_AND_PERSIST = ctypes.c_int(0x03)
LDAP_SYNC_REFRESH_PRESENTS = ctypes.c_int(0)
LDAP_SYNC_REFRESH_DELETES = ctypes.c_int(1)
LDAP_TAG_SYNC_NEW_COOKIE = ctypes.c_uint(0x80)
LDAP_TAG_SYNC_REFRESH_DELETE = ctypes.c_uint(0xa1)
LDAP_TAG_SYNC_REFRESH_PRESENT = ctypes.c_uint(0xa2)
LDAP_TAG_SYNC_ID_SET = ctypes.c_uint(0xa3)
LDAP_TAG_SYNC_COOKIE = ctypes.c_uint(0x04)
LDAP_TAG_REFRESHDELETES = ctypes.c_uint(0x01)
LDAP_TAG_REFRESHDONE = ctypes.c_uint(0x01)
LDAP_TAG_RELOAD_HINT = ctypes.c_uint(0x01)
LDAP_SYNC_PRESENT = ctypes.c_int(0)
LDAP_SYNC_ADD = ctypes.c_int(1)
LDAP_SYNC_MODIFY = ctypes.c_int(2)
LDAP_SYNC_DELETE = ctypes.c_int(3)
LDAP_SYNC_NEW_COOKIE = ctypes.c_int(4)

# Password policy Controls
# work in progress
# ITS#3458: released; disabled by default
LDAP_CONTROL_PASSWORDPOLICYREQUEST = "1.3.6.1.4.1.42.2.27.8.5.1"
LDAP_CONTROL_PASSWORDPOLICYRESPONSE = "1.3.6.1.4.1.42.2.27.8.5.1"

# various works in progress
LDAP_CONTROL_NOOP = "1.3.6.1.4.1.4203.666.5.2"
LDAP_CONTROL_NO_SUBORDINATES = "1.3.6.1.4.1.4203.666.5.11"
LDAP_CONTROL_RELAX = "1.3.6.1.4.1.4203.666.5.12"
LDAP_CONTROL_MANAGEDIT = LDAP_CONTROL_RELAX
LDAP_CONTROL_SLURP = "1.3.6.1.4.1.4203.666.5.13"
LDAP_CONTROL_VALSORT = "1.3.6.1.4.1.4203.666.5.14"
LDAP_CONTROL_DONTUSECOPY = "1.3.6.1.4.1.4203.666.5.15"
LDAP_CONTROL_X_DEREF = "1.3.6.1.4.1.4203.666.5.16"
LDAP_CONTROL_X_WHATFAILED = "1.3.6.1.4.1.4203.666.5.17"

# LDAP Chaining Behavior Control
# work in progress
# <draft-sermersheim-ldap-chaining>;
#  see also LDAP_NO_REFERRALS_FOUND, LDAP_CANNOT_CHAIN
LDAP_CONTROL_X_CHAINING_BEHAVIOR = "1.3.6.1.4.1.4203.666.11.3"
LDAP_CHAINING_PREFERRED = ctypes.c_int(0)
LDAP_CHAINING_REQUIRED = ctypes.c_int(1)
LDAP_REFERRALS_PREFERRED = ctypes.c_int(2)
LDAP_REFERRALS_REQUIRED = ctypes.c_int(3)

# MS Active Directory controls (for compatibility)
LDAP_CONTROL_X_INCREMENTAL_VALUES = "1.2.840.113556.1.4.802"
LDAP_CONTROL_X_DOMAIN_SCOPE = "1.2.840.113556.1.4.1339"
LDAP_CONTROL_X_PERMISSIVE_MODIFY = "1.2.840.113556.1.4.1413"
LDAP_CONTROL_X_SEARCH_OPTIONS = "1.2.840.113556.1.4.1340"
LDAP_SEARCH_FLAG_DOMAIN_SCOPE = ctypes.c_int(1)  # do not generate referrals
LDAP_SEARCH_FLAG_PHANTOM_ROOT = ctypes.c_int(2)  # search all subordinate NCs
LDAP_CONTROL_X_TREE_DELETE = "1.2.840.113556.1.4.805"

# MS Active Directory controls - not implemented in slapd(8)
LDAP_CONTROL_X_EXTENDED_DN = "1.2.840.113556.1.4.529"

# <draft-wahl-ldap-session>
LDAP_CONTROL_X_SESSION_TRACKING = "1.3.6.1.4.1.21008.108.63.1"
LDAP_CONTROL_X_SESSION_TRACKING_RADIUS_ACCT_SESSION_ID = LDAP_CONTROL_X_SESSION_TRACKING + ".1"
LDAP_CONTROL_X_SESSION_TRACKING_RADIUS_ACCT_MULTI_SESSION_ID = LDAP_CONTROL_X_SESSION_TRACKING + ".2"
LDAP_CONTROL_X_SESSION_TRACKING_USERNAME = LDAP_CONTROL_X_SESSION_TRACKING + ".3"

# various expired works
# LDAP Duplicated Entry Control Extension
# not implemented in slapd(8)
LDAP_CONTROL_DUPENT_REQUEST = "2.16.840.1.113719.1.27.101.1"
LDAP_CONTROL_DUPENT_RESPONSE = "2.16.840.1.113719.1.27.101.2"
LDAP_CONTROL_DUPENT_ENTRY = "2.16.840.1.113719.1.27.101.3"
LDAP_CONTROL_DUPENT = LDAP_CONTROL_DUPENT_REQUEST

# LDAP Persistent Search Control
# not implemented in slapd(8)
LDAP_CONTROL_PERSIST_REQUEST = "2.16.840.1.113730.3.4.3"
LDAP_CONTROL_PERSIST_ENTRY_CHANGE_NOTICE = "2.16.840.1.113730.3.4.7"
LDAP_CONTROL_PERSIST_ENTRY_CHANGE_ADD = ctypes.c_int(0x1)
LDAP_CONTROL_PERSIST_ENTRY_CHANGE_DELETE = ctypes.c_int(0x2)
LDAP_CONTROL_PERSIST_ENTRY_CHANGE_MODIFY = ctypes.c_int(0x4)
LDAP_CONTROL_PERSIST_ENTRY_CHANGE_RENAME = ctypes.c_int(0x8)

# LDAP VLV
LDAP_CONTROL_VLVREQUEST = "2.16.840.1.113730.3.4.9"
LDAP_CONTROL_VLVRESPONSE = "2.16.840.1.113730.3.4.10"

# LDAP Unsolicited Notifications
LDAP_NOTICE_OF_DISCONNECTION = "1.3.6.1.4.1.1466.20036"  # RFC 4511
LDAP_NOTICE_DISCONNECT = LDAP_NOTICE_OF_DISCONNECTION

# LDAP Extended Operations
LDAP_EXOP_START_TLS = "1.3.6.1.4.1.1466.20037"  # RFC 4511
LDAP_EXOP_MODIFY_PASSWD = "1.3.6.1.4.1.4203.1.11.1"  # RFC 3062
LDAP_TAG_EXOP_MODIFY_PASSWD_ID = ctypes.c_uint(0x80)
LDAP_TAG_EXOP_MODIFY_PASSWD_OLD = ctypes.c_uint(0x81)
LDAP_TAG_EXOP_MODIFY_PASSWD_NEW = ctypes.c_uint(0x82)
LDAP_TAG_EXOP_MODIFY_PASSWD_GEN = ctypes.c_uint(0x80)
LDAP_EXOP_CANCEL = "1.3.6.1.1.8"  # RFC 3909
LDAP_EXOP_X_CANCEL = LDAP_EXOP_CANCEL
LDAP_EXOP_REFRESH = "1.3.6.1.4.1.1466.101.119.1"  # RFC 2589
LDAP_TAG_EXOP_REFRESH_REQ_DN = ctypes.c_uint(0x80)
LDAP_TAG_EXOP_REFRESH_REQ_TTL = ctypes.c_uint(0x81)
LDAP_TAG_EXOP_REFRESH_RES_TTL = ctypes.c_uint(0x81)
LDAP_EXOP_WHO_AM_I = "1.3.6.1.4.1.4203.1.11.3"  # RFC 4532
LDAP_EXOP_X_WHO_AM_I = LDAP_EXOP_WHO_AM_I

# various works in progress
LDAP_EXOP_TURN = "1.3.6.1.1.19"  # RFC 4531
LDAP_EXOP_X_TURN = LDAP_EXOP_TURN

# LDAP Distributed Procedures <draft-sermersheim-ldap-distproc>
# a work in progress
LDAP_X_DISTPROC_BASE = "1.3.6.1.4.1.4203.666.11.6"
LDAP_EXOP_X_CHAINEDREQUEST = LDAP_X_DISTPROC_BASE + ".1"
LDAP_FEATURE_X_CANCHAINOPS = LDAP_X_DISTPROC_BASE + ".2"
LDAP_CONTROL_X_RETURNCONTREF = LDAP_X_DISTPROC_BASE + ".3"
LDAP_URLEXT_X_LOCALREFOID = LDAP_X_DISTPROC_BASE + ".4"
LDAP_URLEXT_X_REFTYPEOID = LDAP_X_DISTPROC_BASE + ".5"
LDAP_URLEXT_X_SEARCHEDSUBTREEOID = LDAP_X_DISTPROC_BASE + ".6"
LDAP_URLEXT_X_FAILEDNAMEOID = LDAP_X_DISTPROC_BASE + ".7"
LDAP_URLEXT_X_LOCALREF = "x-localReference"
LDAP_URLEXT_X_REFTYPE = "x-referenceType"
LDAP_URLEXT_X_SEARCHEDSUBTREE = "x-searchedSubtree"
LDAP_URLEXT_X_FAILEDNAME = "x-failedName"
LDAP_X_TXN = "1.3.6.1.4.1.4203.666.11.7"  # tmp
LDAP_EXOP_X_TXN_START = LDAP_X_TXN + ".1"
LDAP_CONTROL_X_TXN_SPEC = LDAP_X_TXN + ".2"
LDAP_EXOP_X_TXN_END = LDAP_X_TXN + ".3"
LDAP_EXOP_X_TXN_ABORTED_NOTICE = LDAP_X_TXN + ".4"

# LDAP Features
LDAP_FEATURE_ALL_OP_ATTRS = "1.3.6.1.4.1.4203.1.5.1"  # RFC 3673
LDAP_FEATURE_OBJECTCLASS_ATTRS = "1.3.6.1.4.1.4203.1.5.2"  # @objectClass - new number to be assigned
LDAP_FEATURE_ABSOLUTE_FILTERS = "1.3.6.1.4.1.4203.1.5.3"  # (&) (|)
LDAP_FEATURE_LANGUAGE_TAG_OPTIONS = "1.3.6.1.4.1.4203.1.5.4"
LDAP_FEATURE_LANGUAGE_RANGE_OPTIONS = "1.3.6.1.4.1.4203.1.5.5"
LDAP_FEATURE_MODIFY_INCREMENT = "1.3.6.1.1.14"

# LDAP Experimental (works in progress) Features
LDAP_FEATURE_SUBORDINATE_SCOPE = "1.3.6.1.4.1.4203.666.8.1"  # "children"
LDAP_FEATURE_CHILDREN_SCOPE = LDAP_FEATURE_SUBORDINATE_SCOPE

#  specific LDAP instantiations of BER types we know about
# Overview of LBER tag construction
# 
# 	Bits
# 	______
# 	8 7 | CLASS
# 	0 0 = UNIVERSAL
# 	0 1 = APPLICATION
# 	1 0 = CONTEXT-SPECIFIC
# 	1 1 = PRIVATE
# 		_____
# 		| 6 | DATA-TYPE
# 		  0 = PRIMITIVE
# 		  1 = CONSTRUCTED
# 			___________
# 			| 5 ... 1 | TAG-NUMBER
# general stuff
LDAP_TAG_MESSAGE = ctypes.c_uint(0x30)  # constructed + 16
LDAP_TAG_MSGID = ctypes.c_uint(0x02)  # integer
LDAP_TAG_LDAPDN = ctypes.c_uint(0x04)  # octet string
LDAP_TAG_LDAPCRED = ctypes.c_uint(0x04)  # octet string
LDAP_TAG_CONTROLS = ctypes.c_uint(0xa0)  # context specific + constructed + 0
LDAP_TAG_REFERRAL = ctypes.c_uint(0xa3)  # context specific + constructed + 3
LDAP_TAG_NEWSUPERIOR = ctypes.c_uint(0x80)  # context-specific + primitive + 0
LDAP_TAG_EXOP_REQ_OID = ctypes.c_uint(0x80)  # context specific + primitive
LDAP_TAG_EXOP_REQ_VALUE = ctypes.c_uint(0x81)  # context specific + primitive
LDAP_TAG_EXOP_RES_OID = ctypes.c_uint(0x8a)  # context specific + primitive
LDAP_TAG_EXOP_RES_VALUE = ctypes.c_uint(0x8b)  # context specific + primitive
LDAP_TAG_IM_RES_OID = ctypes.c_uint(0x80)  # context specific + primitive
LDAP_TAG_IM_RES_VALUE = ctypes.c_uint(0x81)  # context specific + primitive
LDAP_TAG_SASL_RES_CREDS = ctypes.c_uint(0x87)  # context specific + primitive

# LDAP Request Messages
#LDAP_REQ_BIND = ctypes.c_uint(0x60)  # application + constructed
#LDAP_REQ_UNBIND = ctypes.c_uint(0x42)  # application + primitive
#LDAP_REQ_SEARCH = ctypes.c_uint(0x63)  # application + constructed
#LDAP_REQ_MODIFY = ctypes.c_uint(0x66)  # application + constructed
#LDAP_REQ_ADD = ctypes.c_uint(0x68)  # application + constructed
#LDAP_REQ_DELETE = ctypes.c_uint(0x4a)  # application + primitive
#LDAP_REQ_MODDN = ctypes.c_uint(0x6c)  # application + constructed
#LDAP_REQ_MODRDN = LDAP_REQ_MODDN
#LDAP_REQ_RENAME = LDAP_REQ_MODDN
#LDAP_REQ_COMPARE = ctypes.c_uint(0x6e)  # application + constructed
#LDAP_REQ_ABANDON = ctypes.c_uint(0x50)  # application + primitive
#LDAP_REQ_EXTENDED = ctypes.c_uint(0x77)  # application + constructed

# LDAP Response Messages
#LDAP_RES_BIND = ctypes.c_uint(0x61)  # application + constructed
#LDAP_RES_SEARCH_ENTRY = ctypes.c_uint(0x64)  # application + constructed
#LDAP_RES_SEARCH_REFERENCE = ctypes.c_uint(0x73)  # V3: application + constructed
#LDAP_RES_SEARCH_RESULT = ctypes.c_uint(0x65)  # application + constructed
#LDAP_RES_MODIFY = ctypes.c_uint(0x67)  # application + constructed
#LDAP_RES_ADD = ctypes.c_uint(0x69)  # application + constructed
#LDAP_RES_DELETE = ctypes.c_uint(0x6b)  # application + constructed
#LDAP_RES_MODDN = ctypes.c_uint(0x6d)  # application + constructed
#LDAP_RES_MODRDN = LDAP_RES_MODDN  # application + constructed
#LDAP_RES_RENAME = LDAP_RES_MODDN  # application + constructed
#LDAP_RES_COMPARE = ctypes.c_uint(0x6f)  # application + constructed
#LDAP_RES_EXTENDED = ctypes.c_uint(0x78)  # V3: application + constructed
#LDAP_RES_INTERMEDIATE = ctypes.c_uint(0x79)  # V3+: application + constructed
#LDAP_RES_ANY = ctypes.c_int(-1)
#LDAP_RES_UNSOLICITED = ctypes.c_int(0)
LDAP_SASL_NULL = ""

# authentication methods available
LDAP_AUTH_NONE = ctypes.c_uint(0x00)  # no authentication
LDAP_AUTH_SIMPLE = ctypes.c_uint(0x80)  # context specific + primitive
LDAP_AUTH_SASL = ctypes.c_uint(0xa3)  # context specific + constructed
LDAP_AUTH_KRBV4 = ctypes.c_uint(0xff)  # means do both of the following
LDAP_AUTH_KRBV41 = ctypes.c_uint(0x81)  # context specific + primitive
LDAP_AUTH_KRBV42 = ctypes.c_uint(0x82)  # context specific + primitive

# used by the Windows API but not used on the wire
LDAP_AUTH_NEGOTIATE = ctypes.c_uint(0x04FF)

# filter types
LDAP_FILTER_AND = ctypes.c_uint(0xa0)  # context specific + constructed
LDAP_FILTER_OR = ctypes.c_uint(0xa1)  # context specific + constructed
LDAP_FILTER_NOT = ctypes.c_uint(0xa2)  # context specific + constructed
LDAP_FILTER_EQUALITY = ctypes.c_uint(0xa3)  # context specific + constructed
LDAP_FILTER_SUBSTRINGS = ctypes.c_uint(0xa4)  # context specific + constructed
LDAP_FILTER_GE = ctypes.c_uint(0xa5)  # context specific + constructed
LDAP_FILTER_LE = ctypes.c_uint(0xa6)  # context specific + constructed
LDAP_FILTER_PRESENT = ctypes.c_uint(0x87)  # context specific + primitive
LDAP_FILTER_APPROX = ctypes.c_uint(0xa8)  # context specific + constructed
LDAP_FILTER_EXT = ctypes.c_uint(0xa9)  # context specific + constructed

# extended filter component types
LDAP_FILTER_EXT_OID = ctypes.c_uint(0x81)  # context specific
LDAP_FILTER_EXT_TYPE = ctypes.c_uint(0x82)  # context specific
LDAP_FILTER_EXT_VALUE = ctypes.c_uint(0x83)  # context specific
LDAP_FILTER_EXT_DNATTRS = ctypes.c_uint(0x84)  # context specific

# substring filter component types
LDAP_SUBSTRING_INITIAL = ctypes.c_uint(0x80)  # context specific
LDAP_SUBSTRING_ANY = ctypes.c_uint(0x81)  # context specific
LDAP_SUBSTRING_FINAL = ctypes.c_uint(0x82)  # context specific

# search scopes
LDAP_SCOPE_BASE = ctypes.c_int(0x0000)
LDAP_SCOPE_BASEOBJECT = LDAP_SCOPE_BASE
LDAP_SCOPE_ONELEVEL = ctypes.c_int(0x0001)
LDAP_SCOPE_ONE = LDAP_SCOPE_ONELEVEL
LDAP_SCOPE_SUBTREE = ctypes.c_int(0x0002)
LDAP_SCOPE_SUB = LDAP_SCOPE_SUBTREE
LDAP_SCOPE_SUBORDINATE = ctypes.c_int(0x0003)  # OpenLDAP extension
LDAP_SCOPE_CHILDREN = LDAP_SCOPE_SUBORDINATE
LDAP_SCOPE_DEFAULT = ctypes.c_int(-1)  # OpenLDAP extension

# substring filter component types
LDAP_SUBSTRING_INITIAL = ctypes.c_uint(0x80)  # context specific
LDAP_SUBSTRING_ANY = ctypes.c_uint(0x81)  # context specific
LDAP_SUBSTRING_FINAL = ctypes.c_uint(0x82)  # context specific

#  LDAP Result Codes
LDAP_SUCCESS = ctypes.c_int(0x00)
LDAP_OPERATIONS_ERROR = ctypes.c_int(0x01)
LDAP_PROTOCOL_ERROR = ctypes.c_int(0x02)
LDAP_TIMELIMIT_EXCEEDED = ctypes.c_int(0x03)
LDAP_SIZELIMIT_EXCEEDED = ctypes.c_int(0x04)
LDAP_COMPARE_FALSE = ctypes.c_int(0x05)
LDAP_COMPARE_TRUE = ctypes.c_int(0x06)
LDAP_AUTH_METHOD_NOT_SUPPORTED = ctypes.c_int(0x07)
LDAP_STRONG_AUTH_NOT_SUPPORTED = LDAP_AUTH_METHOD_NOT_SUPPORTED
LDAP_STRONG_AUTH_REQUIRED = ctypes.c_int(0x08)
LDAP_STRONGER_AUTH_REQUIRED = LDAP_STRONG_AUTH_REQUIRED
LDAP_PARTIAL_RESULTS = ctypes.c_int(0x09)  # LDAPv2+ (not LDAPv3)
LDAP_REFERRAL = ctypes.c_int(0x0a)  # LDAPv3
LDAP_ADMINLIMIT_EXCEEDED = ctypes.c_int(0x0b)  # LDAPv3
LDAP_UNAVAILABLE_CRITICAL_EXTENSION = ctypes.c_int(0x0c)  # LDAPv3
LDAP_CONFIDENTIALITY_REQUIRED = ctypes.c_int(0x0d)  # LDAPv3
LDAP_SASL_BIND_IN_PROGRESS = ctypes.c_int(0x0e)  # LDAPv3
###LDAP_ATTR_ERROR(n) = LDAP_RANGE
LDAP_NO_SUCH_ATTRIBUTE = ctypes.c_int(0x10)
LDAP_UNDEFINED_TYPE = ctypes.c_int(0x11)
LDAP_INAPPROPRIATE_MATCHING = ctypes.c_int(0x12)
LDAP_CONSTRAINT_VIOLATION = ctypes.c_int(0x13)
LDAP_TYPE_OR_VALUE_EXISTS = ctypes.c_int(0x14)
LDAP_INVALID_SYNTAX = ctypes.c_int(0x15)
###LDAP_NAME_ERROR(n) = LDAP_RANGE
LDAP_NO_SUCH_OBJECT = ctypes.c_int(0x20)
LDAP_ALIAS_PROBLEM = ctypes.c_int(0x21)
LDAP_INVALID_DN_SYNTAX = ctypes.c_int(0x22)
LDAP_IS_LEAF = ctypes.c_int(0x23)  # not LDAPv3
LDAP_ALIAS_DEREF_PROBLEM = ctypes.c_int(0x24)
###LDAP_SECURITY_ERROR(n) = LDAP_RANGE
LDAP_X_PROXY_AUTHZ_FAILURE = ctypes.c_int(0x2F)  # LDAPv3 proxy authorization
LDAP_INAPPROPRIATE_AUTH = ctypes.c_int(0x30)
LDAP_INVALID_CREDENTIALS = ctypes.c_int(0x31)
LDAP_INSUFFICIENT_ACCESS = ctypes.c_int(0x32)
###LDAP_SERVICE_ERROR(n) = LDAP_RANGE
LDAP_BUSY = ctypes.c_int(0x33)
LDAP_UNAVAILABLE = ctypes.c_int(0x34)
LDAP_UNWILLING_TO_PERFORM = ctypes.c_int(0x35)
LDAP_LOOP_DETECT = ctypes.c_int(0x36)
###LDAP_UPDATE_ERROR(n) = LDAP_RANGE
LDAP_NAMING_VIOLATION = ctypes.c_int(0x40)
LDAP_OBJECT_CLASS_VIOLATION = ctypes.c_int(0x41)
LDAP_NOT_ALLOWED_ON_NONLEAF = ctypes.c_int(0x42)
LDAP_NOT_ALLOWED_ON_RDN = ctypes.c_int(0x43)
LDAP_ALREADY_EXISTS = ctypes.c_int(0x44)
LDAP_NO_OBJECT_CLASS_MODS = ctypes.c_int(0x45)
LDAP_RESULTS_TOO_LARGE = ctypes.c_int(0x46)  # CLDAP
LDAP_AFFECTS_MULTIPLE_DSAS = ctypes.c_int(0x47)
LDAP_VLV_ERROR = ctypes.c_int(0x4C)
LDAP_OTHER = ctypes.c_int(0x50)

# LCUP operation codes (113-117) - not implemented
LDAP_CUP_RESOURCES_EXHAUSTED = ctypes.c_int(0x71)
LDAP_CUP_SECURITY_VIOLATION = ctypes.c_int(0x72)
LDAP_CUP_INVALID_DATA = ctypes.c_int(0x73)
LDAP_CUP_UNSUPPORTED_SCHEME = ctypes.c_int(0x74)
LDAP_CUP_RELOAD_REQUIRED = ctypes.c_int(0x75)

# Cancel operation codes (118-121)
LDAP_CANCELLED = ctypes.c_int(0x76)
LDAP_NO_SUCH_OPERATION = ctypes.c_int(0x77)
LDAP_TOO_LATE = ctypes.c_int(0x78)
LDAP_CANNOT_CANCEL = ctypes.c_int(0x79)

# Assertion control (122)
LDAP_ASSERTION_FAILED = ctypes.c_int(0x7A)

# Proxied Authorization Denied (123)
LDAP_PROXIED_AUTHORIZATION_DENIED = ctypes.c_int(0x7B)

# Experimental result codes
###LDAP_E_ERROR(n) = LDAP_RANGE

# LDAP Sync (4096)
LDAP_SYNC_REFRESH_REQUIRED = ctypes.c_int(0x1000)

# Private Use result codes
###LDAP_X_ERROR(n) = LDAP_RANGE
LDAP_X_SYNC_REFRESH_REQUIRED = ctypes.c_int(0x4100)  # defunct
LDAP_X_ASSERTION_FAILED = ctypes.c_int(0x410f)  # defunct

# for the LDAP No-Op control
LDAP_X_NO_OPERATION = ctypes.c_int(0x410e)
LDAP_X_NO_REFERRALS_FOUND = ctypes.c_int(0x4110)
LDAP_X_CANNOT_CHAIN = ctypes.c_int(0x4111)
LDAP_X_INVALIDREFERENCE = ctypes.c_int(0x4112)
LDAP_X_TXN_SPECIFY_OKAY = ctypes.c_int(0x4120)
LDAP_X_TXN_ID_INVALID = ctypes.c_int(0x4121)
LDAP_SERVER_DOWN = ctypes.c_int(-1)
LDAP_LOCAL_ERROR = ctypes.c_int(-2)
LDAP_ENCODING_ERROR = ctypes.c_int(-3)
LDAP_DECODING_ERROR = ctypes.c_int(-4)
LDAP_TIMEOUT = ctypes.c_int(-5)
LDAP_AUTH_UNKNOWN = ctypes.c_int(-6)
LDAP_FILTER_ERROR = ctypes.c_int(-7)
LDAP_USER_CANCELLED = ctypes.c_int(-8)
LDAP_PARAM_ERROR = ctypes.c_int(-9)
LDAP_NO_MEMORY = ctypes.c_int(-10)
LDAP_CONNECT_ERROR = ctypes.c_int(-11)
LDAP_NOT_SUPPORTED = ctypes.c_int(-12)
LDAP_CONTROL_NOT_FOUND = ctypes.c_int(-13)
LDAP_NO_RESULTS_RETURNED = ctypes.c_int(-14)
LDAP_MORE_RESULTS_TO_RETURN = ctypes.c_int(-15)  # Obsolete
LDAP_CLIENT_LOOP = ctypes.c_int(-16)
LDAP_REFERRAL_LIMIT_EXCEEDED = ctypes.c_int(-17)
LDAP_X_CONNECTING = ctypes.c_int(-18)
LDAP_MOD_OP = ctypes.c_int(0x0007)
LDAP_MOD_ADD = ctypes.c_int(0x0000)
LDAP_MOD_DELETE = ctypes.c_int(0x0001)
LDAP_MOD_REPLACE = ctypes.c_int(0x0002)
LDAP_MOD_INCREMENT = ctypes.c_int(0x0003)  # OpenLDAP extension
LDAP_MOD_BVALUES = ctypes.c_int(0x0080)
#mod_values = mod_vals.modv_strvals
#mod_bvalues = mod_vals.modv_bvals
LDAP_DEREF_NEVER = ctypes.c_int(0x00)
LDAP_DEREF_SEARCHING = ctypes.c_int(0x01)
LDAP_DEREF_FINDING = ctypes.c_int(0x02)
LDAP_DEREF_ALWAYS = ctypes.c_int(0x03)
LDAP_NO_LIMIT = ctypes.c_int(0)

# how many messages to retrieve results for
LDAP_MSG_ONE = ctypes.c_int(0x00)
LDAP_MSG_ALL = ctypes.c_int(0x01)
LDAP_MSG_RECEIVED = ctypes.c_int(0x02)
LDAP_URL_SUCCESS = ctypes.c_int(0x00)  # Success
LDAP_URL_ERR_MEM = ctypes.c_int(0x01)  # can't allocate memory space
LDAP_URL_ERR_PARAM = ctypes.c_int(0x02)  # parameter is bad
LDAP_URL_ERR_BADSCHEME = ctypes.c_int(0x03)  # URL doesn't begin with "ldap[si]://"
LDAP_URL_ERR_BADENCLOSURE = ctypes.c_int(0x04)  # URL is missing trailing ">"
LDAP_URL_ERR_BADURL = ctypes.c_int(0x05)  # URL is bad
LDAP_URL_ERR_BADHOST = ctypes.c_int(0x06)  # host port is bad
LDAP_URL_ERR_BADATTRS = ctypes.c_int(0x07)  # bad (or missing) attributes
LDAP_URL_ERR_BADSCOPE = ctypes.c_int(0x08)  # scope string is invalid (or missing)
LDAP_URL_ERR_BADFILTER = ctypes.c_int(0x09)  # bad or missing filter
LDAP_URL_ERR_BADEXTS = ctypes.c_int(0x0a)  # bad or missing extensions

# Interaction flags (should be passed about in a control)
#   Automatic (default): use defaults, prompt otherwise
#   Interactive: prompt always
#   Quiet: never prompt
LDAP_SASL_AUTOMATIC = ctypes.c_uint(0)
LDAP_SASL_INTERACTIVE = ctypes.c_uint(1)
LDAP_SASL_QUIET = ctypes.c_uint(2)
LDAP_AVA_NULL = ctypes.c_uint(0x0000)
LDAP_AVA_STRING = ctypes.c_uint(0x0001)
LDAP_AVA_BINARY = ctypes.c_uint(0x0002)
LDAP_AVA_NONPRINTABLE = ctypes.c_uint(0x0004)
LDAP_AVA_FREE_ATTR = ctypes.c_uint(0x0010)
LDAP_AVA_FREE_VALUE = ctypes.c_uint(0x0020)

# DN formats
LDAP_DN_FORMAT_LDAP = ctypes.c_uint(0x0000)
LDAP_DN_FORMAT_LDAPV3 = ctypes.c_uint(0x0010)
LDAP_DN_FORMAT_LDAPV2 = ctypes.c_uint(0x0020)
LDAP_DN_FORMAT_DCE = ctypes.c_uint(0x0030)
LDAP_DN_FORMAT_UFN = ctypes.c_uint(0x0040)  # dn2str only
LDAP_DN_FORMAT_AD_CANONICAL = ctypes.c_uint(0x0050)  # dn2str only
LDAP_DN_FORMAT_LBER = ctypes.c_uint(0x00F0)  # for testing only
LDAP_DN_FORMAT_MASK = ctypes.c_uint(0x00F0)

# DN flags
LDAP_DN_PRETTY = ctypes.c_uint(0x0100)
LDAP_DN_SKIP = ctypes.c_uint(0x0200)
LDAP_DN_P_NOLEADTRAILSPACES = ctypes.c_uint(0x1000)
LDAP_DN_P_NOSPACEAFTERRDN = ctypes.c_uint(0x2000)
LDAP_DN_PEDANTIC = ctypes.c_uint(0xF000)

#  LDAP Cancel Extended Operation <draft-zeilenga-ldap-cancel-xx.txt>
#   in cancel.c
LDAP_API_FEATURE_CANCEL = ctypes.c_int(1000)

#  LDAP Turn Extended Operation <draft-zeilenga-ldap-turn-xx.txt>
#   in turn.c
LDAP_API_FEATURE_TURN = ctypes.c_int(1000)

#  LDAP Paged Results
# 	in pagectrl.c
LDAP_API_FEATURE_PAGED_RESULTS = ctypes.c_int(2000)

#  LDAP Server Side Sort
# 	in sortctrl.c
LDAP_API_FEATURE_SERVER_SIDE_SORT = ctypes.c_int(2000)

#  LDAP Virtual List View
# 	in vlvctrl.c
LDAP_API_FEATURE_VIRTUAL_LIST_VIEW = ctypes.c_int(2000)

#  LDAP Who Am I?
# 	in whoami.c
LDAP_API_FEATURE_WHOAMI = ctypes.c_int(1000)

#  LDAP Password Modify
# 	in passwd.c
LDAP_API_FEATURE_PASSWD_MODIFY = ctypes.c_int(1000)

#  LDAP Password Policy controls
# 	in ppolicy.c
LDAP_API_FEATURE_PASSWORD_POLICY = ctypes.c_int(1000)

#  LDAP Dynamic Directory Services Refresh -- RFC 2589
# 	in dds.c
LDAP_API_FEATURE_REFRESH = ctypes.c_int(1000)
import ctypes


#LDAP_LEVEL_EMERG = ldap_syslog_level
#LDAP_LEVEL_ALERT = ldap_syslog_level
#LDAP_LEVEL_CRIT = ldap_syslog_level
#LDAP_LEVEL_ERR = ldap_syslog_level
#LDAP_LEVEL_WARNING = ldap_syslog_level
#LDAP_LEVEL_NOTICE = ldap_syslog_level
#LDAP_LEVEL_INFO = ldap_syslog_level
#LDAP_LEVEL_DEBUG = ldap_syslog_level
#LDAP_LEVEL_EMERG = ctypes.c_int(7)
#LDAP_LEVEL_ALERT = ctypes.c_int(7)
#LDAP_LEVEL_CRIT = ctypes.c_int(7)
#LDAP_LEVEL_ERR = ctypes.c_int(7)
#LDAP_LEVEL_WARNING = ctypes.c_int(7)
#LDAP_LEVEL_NOTICE = ctypes.c_int(7)
#LDAP_LEVEL_INFO = ctypes.c_int(7)
#LDAP_LEVEL_DEBUG = ctypes.c_int(7)
#LDAP_LEVEL_EMERG = LOG_EMERG
#LDAP_LEVEL_ALERT = LOG_ALERT
#LDAP_LEVEL_CRIT = LOG_CRIT
#LDAP_LEVEL_ERR = LOG_ERR
#LDAP_LEVEL_WARNING = LOG_WARNING
#LDAP_LEVEL_NOTICE = LOG_NOTICE
#LDAP_LEVEL_INFO = LOG_INFO
#LDAP_LEVEL_DEBUG = LOG_DEBUG
#LDAP_LEVEL_EMERG = ctypes.c_int(0)
#LDAP_LEVEL_ALERT = ctypes.c_int(1)
#LDAP_LEVEL_CRIT = ctypes.c_int(2)
#LDAP_LEVEL_ERR = ctypes.c_int(3)
#LDAP_LEVEL_WARNING = ctypes.c_int(4)
#LDAP_LEVEL_NOTICE = ctypes.c_int(5)
#LDAP_LEVEL_INFO = ctypes.c_int(6)
#LDAP_LEVEL_DEBUG = ctypes.c_int(7)
###LDAP_LEVEL_MASK(s) = s

# (yet) unused
#LDAP_LEVEL_ENTRY = ctypes.c_int(0x08)  # log function entry points
#LDAP_LEVEL_ARGS = ctypes.c_int(0x10)  # log function call parameters
#LDAP_LEVEL_RESULTS = ctypes.c_int(0x20)  # Log function results
#LDAP_LEVEL_DETAIL1 = ctypes.c_int(0x40)  # log level 1 function operational details
#LDAP_LEVEL_DETAIL2 = ctypes.c_int(0x80)  # Log level 2 function operational details

# end of (yet) unused
# original subsystem selection mechanism
LDAP_DEBUG_TRACE = ctypes.c_int(0x0001)
LDAP_DEBUG_PACKETS = ctypes.c_int(0x0002)
LDAP_DEBUG_ARGS = ctypes.c_int(0x0004)
LDAP_DEBUG_CONNS = ctypes.c_int(0x0008)
LDAP_DEBUG_BER = ctypes.c_int(0x0010)
LDAP_DEBUG_FILTER = ctypes.c_int(0x0020)
LDAP_DEBUG_CONFIG = ctypes.c_int(0x0040)
LDAP_DEBUG_ACL = ctypes.c_int(0x0080)
LDAP_DEBUG_STATS = ctypes.c_int(0x0100)
LDAP_DEBUG_STATS2 = ctypes.c_int(0x0200)
LDAP_DEBUG_SHELL = ctypes.c_int(0x0400)
LDAP_DEBUG_PARSE = ctypes.c_int(0x0800)
LDAP_DEBUG_CACHE = ctypes.c_int(0x1000)
LDAP_DEBUG_INDEX = ctypes.c_int(0x2000)
LDAP_DEBUG_SYNC = ctypes.c_int(0x4000)
LDAP_DEBUG_NONE = ctypes.c_int(0x8000)
LDAP_DEBUG_ANY = ctypes.c_int(-1)
#syslog = eb_syslog
###Log0( = level, + severity, + fmt
###Log1( = level, + severity, + fmt, + arg1
###Log2( = level, + severity, + fmt, + arg1, + arg2
###Log3( = level, + severity, + fmt, + arg1, + arg2, + arg3
###Log4( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4
###Log5( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4, + arg5
###Debug( = level, + fmt, + arg1, + arg2, + arg3
###Log0( = level, + severity, + fmt
###Log1( = level, + severity, + fmt, + arg1
###Log2( = level, + severity, + fmt, + arg1, + arg2
###Log3( = level, + severity, + fmt, + arg1, + arg2, + arg3
###Log4( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4
###Log5( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4, + arg5
###Debug( = level, + fmt, + arg1, + arg2, + arg3

# TODO: in case LDAP_DEBUG is undefined, make sure logs with appropriate
#  severity gets thru anyway
###Log0( = level, + severity, + fmt
###Log1( = level, + severity, + fmt, + arg1
###Log2( = level, + severity, + fmt, + arg1, + arg2
###Log3( = level, + severity, + fmt, + arg1, + arg2, + arg3
###Log4( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4
###Log5( = level, + severity, + fmt, + arg1, + arg2, + arg3, + arg4, + arg5
###Debug( = level, + fmt, + arg1, + arg2, + arg3
