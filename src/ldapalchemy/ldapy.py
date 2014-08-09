from __future__ import absolute_import, division, print_function, unicode_literals

import ctypes as ct

from . import exceptions as excs

from ._defines import *
from .exceptions import *
from ._libldap import libldap


ERRORS = dict((exc.code, exc) for exc in
              (getattr(excs, name) for name in dir(excs))
              if hasattr(exc, 'code'))


def error(rc, *args, **kw):
    try:
        return ERRORS[rc](*args, **kw)
    except KeyError:
        return excs.YetUnspecified(rc)


def initialize(uri=None, start_tls=True):
    """Initialize ldap session using LDAPv3

    Return an ldap session handle or raise an LDAPError.

    """
    ld = ct.c_void_p()
    if uri is not None:
        uri = uri.encode('utf-8')

    # For ldaps tls is started already and for ldapi it makes no sense
    start_tls = start_tls and uri and uri.startswith('ldap:')

    # initialize connection
    rc = libldap.ldap_initialize(ct.byref(ld), uri)
    if rc != 0:
        if ld.value is not None:
            libldap.ldap_unbind(ld)
        raise error(rc)

    # wrap options properly so they can be passed to initialize
    #
    # XXX: from . import opts; opts.DEBUG_LEVEL
    # or: from ._defines import opts
    #
    # XXX: then again 'man ldap_get_option' is helpful and one could
    # argue to stick here as close as possible to the C API

    # enable logging
    set_option(ld, LDAP_OPT_DEBUG_LEVEL, LDAP_DEBUG_ANY)

    # switch to LDAPv3
    set_option(ld, LDAP_OPT_PROTOCOL_VERSION, LDAP_VERSION3)

    if start_tls:
        # Don't validate server certificate, i.e. allow self-signed
        # XXX: does not work, using ldaprc for now
        # set_option(ld, LDAP_OPT_X_TLS_REQUIRE_CERT, LDAP_OPT_X_TLS_ALLOW)
        serverctrls = None
        clientctrls = None
        rc = libldap.ldap_start_tls_s(ld, serverctrls, clientctrls)
        if rc != 0:
            msg = ct.c_char_p()
            libldap.ldap_get_option(ld, LDAP_OPT_DIAGNOSTIC_MESSAGE, ct.byref(msg))
            info = msg.value
            libldap.ldap_memfree(msg)
            libldap.ldap_unbind(ld)
            raise error(rc, info=info)

    return ld


# def get_option(ld, opt):
#     value = ct.c_void_p()
#     rc = libldap.ldap_get_option(ld, opt, value)
#     if rc != 0:
#         libldap.ldap_unbind(ld)
#         raise error(rc)
#     return value


def set_option(ld, opt, value):
    rc = libldap.ldap_set_option(ld, opt, ct.byref(value))
    if rc != 0:
        libldap.ldap_unbind(ld)
        raise error(rc)


def simple_bind_s(ld, dn, pw):
    rc = libldap.ldap_simple_bind_s(ld, dn.encode('utf-8'), pw.encode('utf-8'))
    if rc != 0:
        libldap.ldap_unbind(ld)
        raise error(rc)

unbind = libldap.ldap_unbind
