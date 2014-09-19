"""pythonic ldap

Work in Progress
"""

__author__ = 'Florian Friesdorf <flo@chaoflow.net>'
__version__ = '0.20140726'


import ctypes as ct


try:
    libldap = ct.CDLL('libldap.so')
except OSError:
    libldap = ct.CDLL('libldap.dylib')
