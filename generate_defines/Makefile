all: _parser.py

ldaph.pretty.ebnf: ldaph.ebnf
	../venv27/bin/python -m grako -p $< >$@

diff-pretty: ldaph.pretty.ebnf
	diff -u ldaph.ebnf ldaph.pretty.ebnf

use-pretty: ldaph.pretty.ebnf 
	mv $< ldaph.ebnf

_parser.py: ldaph.ebnf
	../venv27/bin/python -m grako $< > $@

parse: _parser.py
	../venv27/bin/python _parser.py ../env/include/ldap.h defines

