"""Waiting for cffi support for defines and general production readiness
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import grako
import itertools
import json
import sys

from collections import OrderedDict

from . import _parser


class Define(object):
    def __init__(self, symbol, value, prologue=None, comment=None):
        self.symbol = symbol
        self.value = value
        self.prologue = prologue
        self.comment = comment

    @property
    def as_dict(self):
        return dict(symbol=self.symbol, value=self.value,
                    prologue=self.prologue, comment=self.comment)

    @property
    def as_python(self):
        rv = '%s = %s' % (self.symbol, self.value)
        if self.prologue:
            rv = '\n' + '\n'.join(['# ' + x for x in self.prologue] + [ rv ])
        if self.comment:
            rv = '  # '.join([rv, self.comment])
        return rv


class Parser(_parser.ldaphParser):
    def __init__(self, **kw):
        super(Parser, self).__init__(**kw)

    def parse(self, *args, **kw):
        kw.setdefault('semantics', Semantics())
        return super(Parser, self).parse(*args, **kw)


class Semantics(grako.model.ModelBuilderSemantics):
    def define(self, ast, _):
        value = ' + '.join(ast.value)
        if value.endswith('U'):
            value = 'ctypes.c_uint(%s)' % value.rstrip('U')
        else:
            try:
                if 'x' in value:
                    int(value, 16)
                else:
                    int(value)
            except ValueError:
                pass
            else:
                value = 'ctypes.c_int(%s)' % value
        kw = dict(
            value=value,
            prologue=tuple(x.lstrip().lstrip('*')
                           for x in '\n'.join(ast.prologue).split('\n')
                           if x),
            comment=ast.comment)

        if '(' in ast.symbol:
            return Define(symbol='###' + ast.symbol, **kw)
        elif ast.symbol[0].islower() \
             or value == 'LDAP_VENDOR_VERSION' \
             or ast.symbol.startswith('LDAP_REQ_') \
             or ast.symbol.startswith('LDAP_RES_') \
             or ast.symbol.startswith('LDAP_LEVEL'):
            return Define(symbol='#' + ast.symbol, **kw)
        else:
            return Define(symbol=ast.symbol, **kw)


def main():
    parser = Parser(trace=False, whitespace='')
    with open(sys.argv[1], 'rv') as infile:
        ast = parser.parse(infile.read().decode('utf-8').replace('\\\n', ''), 'defines')

    #print(json.dumps(ast, indent=2, default=lambda x: x.as_dict))

    print('import ctypes\n\n')
    print('\n'.join(x.as_python for x in ast))

if __name__ == '__main__':
    main()
    sys.exit(0)
