from __future__ import absolute_import, division, print_function, unicode_literals

"""XXX: import libldap for some reason becomes the CDLL
"""

import ctypes

try:
    libldap = ctypes.CDLL('libldap.so')
except OSError:
    libldap = ctypes.CDLL('libldap.dylib')
libldap.ldap_err2string.restype = ctypes.c_char_p
