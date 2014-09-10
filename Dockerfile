FROM		centos:centos7
MAINTAINER 	Jussi Talaskivi <jussi.talaskivi@jyu.fi>

RUN		yum -y install git make python-setuptools openldap-servers openldap-devel openldap-clients openssl-devel tar patch which zlib-devel python-devel bzip2 gcc-c++ libjpeg-devel libxslt-devel readline-devel; true
RUN		easy_install virtualenv
ADD		. /ldapalchemy
ADD		etc/openldap /etc/openldap
ADD		ldaprc /etc/openldap/ldap.conf
WORKDIR		/ldapalchemy
RUN		make
