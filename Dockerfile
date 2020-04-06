FROM centos:centos7
MAINTAINER The CentOS Project <cloud-ops@centos.org>

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python python-devel python-pip
RUN yum -y install git gcc
RUN yum -y install openldap openldap-devel openldap-servers openldap-clients
RUN yum clean all

RUN pip install --upgrade pip
RUN pip install "django>1.11,<2" "chardet<4,>=3.0.2"

# Make sure to have the correct version
ADD django-ldapdb /opt/django-ldapdb

WORKDIR /opt/django-ldapdb
RUN pip install -r requirements_dev.txt

CMD ["python", "setup.py", "test"]
