FROM		centos:centos7
MAINTAINER 	Jussi Talaskivi <jussi.talaskivi@jyu.fi>

RUN		yum -y install http://hydra.nixos.org/build/10272854/download/3/nix-1.7-2.fc19.x86_64.rpm
RUN		yum -y install git make python-setuptools openldap-servers openldap-devel; true
RUN		easy_install virtualenv
RUN		git clone https://github.com/chaoflow/ldapalchemy.git
WORKDIR		/ldapalchemy
RUN		make
