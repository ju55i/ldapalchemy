from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'Florian Friesdorf <flo@chaoflow.net>'
__version__ = '0.20140726'

from . import libldap


class Connection(object):
    def __init__(self, uri):
        self.uri = uri
        self.ld = libldap.ldap_initialize(uri)

    def bind(self, dn, pw):
        self.dn = dn
        self.pw = pw
        libldap.ldap_simple_bind_s(self.ld, dn, pw)
