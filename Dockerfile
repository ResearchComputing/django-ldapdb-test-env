FROM centos:centos8
MAINTAINER Aaron Holt aaron.holt@colorado.edu

RUN dnf -y update
RUN dnf -y install epel-release
RUN dnf -y install python3 python3-devel python3-pip
RUN dnf -y install git gcc wget

RUN dnf -y install openldap openldap-devel

RUN wget -q https://repo.symas.com/configs/SOFL/rhel8/sofl.repo -O /etc/yum.repos.d/sofl.repo && \
    yum update
RUN dnf -y install symas-openldap-clients symas-openldap-servers

#RUN dnf -y install epel-release
## make sure you have the latest epel-release that contains modular repositories
#RUN dnf -y update epel-release
#RUN dnf -y module install 389-directory-server:stable/default

RUN dnf clean all

RUN pip3 install --upgrade pip
RUN pip3 install "django>=2,<3" "chardet<4,>=3.0.2" "volatildap>=1.1.0" "factory_boy==2.12.0"
RUN pip3 install check-manifest flake8 isort tox wheel zest.releaser
#RUN (export PYTHONIOENCODING=UTF-8 && export LC_ALL=C && pip3 install factory_boy==2.12.0) 
RUN pip3 install pyasn1 pyasn1-modules pyroma "python-ldap>=3"

# Make sure to have the correct version
RUN mkdir /opt/django-ldapdb
COPY ./ /opt/django-ldapdb/

WORKDIR /opt/django-ldapdb
RUN pip3 install -r requirements_dev.txt

CMD ["python3", "setup.py", "test"]
