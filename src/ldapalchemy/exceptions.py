"""Exceptions for  errors

Taken in blocks from ldap.h as experienced.

"""

from __future__ import absolute_import, division, print_function, unicode_literals

from ._libldap import libldap


class Error(Exception):
    def __init__(self, info=None):
        self.info = info

    @property
    def msg(self):
        # XXX: untangle this
        try:
            msg = libldap.ldap_err2string(self.code)
        except:
            msg = "Error resolving error code '%s'" % self.code
        if self.info:
            msg = "%s\n  %s" % (msg, self.info)
        return msg

    def __str__(self):
        return self.msg


class YetUnspecified(Error):
    def __init__(self, rc):
        self.code = rc


class OperationsError(Error):
    code = 0x01


class ProtocolError(Error):
    code = 0x02


class TimelimitExceeded(Error):
    code = 0x03


class SizelimitExceeded(Error):
    code = 0x04


class CompareFalse(Error):
    code = 0x05


class CompareTrue(Error):
    code = 0x06


class AuthMethodNotSupported(Error):
    code = 0x07


class StrongAuthRequired(Error):
    code = 0x08


class Referral(Error):
    code = 0x0a


class AdminlimitExceeded(Error):
    code = 0x0b


class UnavailableCriticalExtension(Error):
    code = 0x0c


class ConfidentialityRequired(Error):
    code = 0x0d


class SaslBindInProgress(Error):
    code = 0x0e


class AttrError(Error):
    pass


class NoSuchAttribute(AttrError):
    code = 0x10


class UndefinedType(AttrError):
    code = 0x11


class InappropriateMatching(AttrError):
    code = 0x12


class ConstraintViolation(AttrError):
    code = 0x13


class TypeOrValueExists(AttrError):
    code = 0x14


class InvalidSyntax(AttrError):
    code = 0x15


class NameError(Error):
    pass


class NoSuchObject(NameError):
    code = 0x20


class AliasProblem(NameError):
    code = 0x21


class InvalidDNSyntax(NameError):
    code = 0x22


class AliasDerefProblem(NameError):
    code = 0x24


class SecurityError(Error):
    pass


class ProxyAuthzFailure(SecurityError):
    code = 0x2F


class InappropriateAuth(SecurityError):
    code = 0x30


class InvalidCredentials(SecurityError):
    code = 0x31


class InsufficientAccess(SecurityError):
    code = 0x32


class ServiceError(Error):
    pass


class Busy(ServiceError):
    code = 0x33


class Unavailable(ServiceError):
    code = 0x34


class UnwillingToPerform(ServiceError):
    code = 0x35


class LoopDetect(ServiceError):
    code = 0x36


class APIError(Error):
    pass


class ServerDown(APIError):
    code = -1


class LocalError(APIError):
    code = -2


class EncodingError(APIError):
    code = -3


class DecodingError(APIError):
    code = -4


class Timeout(APIError):
    code = -5


class AuthUnknown(APIError):
    code = -6


class FilterError(APIError):
    code = -7


class UserCancelled(APIError):
    code = -8


class ParamError(APIError):
    code = -9


class NoMemory(APIError):
    code = -10


class ConnectError(APIError):
    code = -11


class NotSupported(APIError):
    code = -12


class ControlNotFound(APIError):
    code = -13


class NoResultsReturned(APIError):
    code = -14


# obsolete according to ldap.h
class MoreResultsToReturn(APIError):
    code = -15


class ClientLoop(APIError):
    code = -16


class ReferralLimitExceeded(APIError):
    code = -17


class XConnecting(APIError):
    code = -18
