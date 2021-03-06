#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import graken, Parser


__version__ = (2014, 9, 4, 13, 27, 3, 3)

__all__ = [
    'ldaphParser',
    'ldaphSemantics',
    'main'
]


class ldaphParser(Parser):
    def __init__(self, whitespace=None, nameguard=True, **kwargs):
        super(ldaphParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            **kwargs
        )

    @graken()
    def _defines_(self):

        def block0():
            with self._choice():
                with self._option():
                    self._define_()
                    self.ast.setlist('@', self.last_node)
                with self._option():
                    self._ignore_()
                self._error('no available options')
        self._positive_closure(block0)

        self._check_eof()

    @graken()
    def _comment_(self):
        self._pattern(r'\/\*\s*')
        self._cut()
        self._pattern(r'(?:.|\n)*?(?=\s*\*\/)')
        self.ast['@'] = self.last_node
        self._pattern(r'\s*\*\/')

    @graken()
    def _trailing_comment_(self):
        self._pattern(r'\/\*\s*')
        self._cut()
        self._pattern(r'.*?(?=\s*\*\/)')
        self.ast['@'] = self.last_node
        self._pattern(r'\s*\*\/')

    @graken('Define')
    def _define_(self):

        def block0():
            self._comment_()
            self.ast.setlist('prologue', self.last_node)
            self._pattern(r'[ \t\n]*')
        self._closure(block0)
        self._token('#define')
        self._pattern(r'[ \t]+')
        self._symbol_()
        self.ast['symbol'] = self.last_node

        def block3():
            self._pattern(r'[ \t]+')
            self._value_()
            self.ast.setlist('value', self.last_node)
        self._positive_closure(block3)

        with self._optional():
            self._pattern(r'[ \t]*')
            self._trailing_comment_()
            self.ast['comment'] = self.last_node
        self._pattern(r'\n?')

        self.ast._define(
            ['symbol', 'comment'],
            ['prologue', 'value']
        )

    @graken()
    def _symbol_(self):
        self._pattern(r'[^\s]+')

    @graken()
    def _value_(self):
        with self._choice():
            with self._option():
                self._token('((')
                self._pattern(r'[^\s]+\)\s')
                self._pattern(r'[^\s\/()]+')
                self.ast['@'] = self.last_node
                self._token(')')
            with self._option():
                self._token('(')
                self._pattern(r'[^\s\/()]+')
                self.ast['@'] = self.last_node
                self._token(')')
            with self._option():
                self._pattern(r'[^\s\/()]+')
                self.ast['@'] = self.last_node
            self._error('expecting one of: ( (( [^\\s\\/()]+')

    @graken()
    def _ignore_(self):
        self._pattern(r'[^\n]*\n?')


class ldaphSemantics(object):
    def defines(self, ast):
        return ast

    def comment(self, ast):
        return ast

    def trailing_comment(self, ast):
        return ast

    def define(self, ast):
        return ast

    def symbol(self, ast):
        return ast

    def value(self, ast):
        return ast

    def ignore(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = ldaphParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in ldaphParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for ldaph.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace
    )

