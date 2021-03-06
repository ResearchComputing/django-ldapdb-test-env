FROM centos:centos7
MAINTAINER The CentOS Project <cloud-ops@centos.org>

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python python-devel python-pip
RUN yum -y install git gcc
RUN yum -y install openldap openldap-devel openldap-servers openldap-clients
RUN yum clean all

RUN pip install --upgrade pip
RUN pip install "django>1.11,<2" "chardet<4,>=3.0.2" "volatildap>=1.1.0"
RUN pip install check-manifest flake8 factory_boy isort tox wheel zest.releaser
RUN pip install pyasn1 pyasn1-modules pyroma "python-ldap>=3"

# Make sure to have the correct version
RUN mkdir /opt/django-ldapdb
COPY ./ /opt/django-ldapdb/

WORKDIR /opt/django-ldapdb
RUN pip install -r requirements_dev.txt

CMD ["python", "setup.py", "test"]
