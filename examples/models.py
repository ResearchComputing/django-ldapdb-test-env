# -*- coding: utf-8 -*-
# This software is distributed under the two-clause BSD license.
# Copyright (c) The django-ldapdb project

from __future__ import unicode_literals

import ldapdb.models
from ldapdb.models import fields


class RCLdapUser(ldapdb.models.Model):
    """
    Class for representing an LDAP user entry.
    """
    rdn_keys = ['username']

    # LDAP meta-data
    base_dn = 'ou=users,dc=example,dc=org'
    object_classes = ['posixAccount', 'inetOrgPerson']
    last_modified = fields.DateTimeField(db_column='modifyTimestamp')

    organization = fields.CharField(max_length=128,blank=False,null=False)

    # inetOrgPerson
    first_name = fields.CharField(db_column='givenName', verbose_name="Prime name")
    last_name = fields.CharField("Final name", db_column='sn')
    full_name = fields.CharField(db_column='cn')
    email = fields.CharField(db_column='mail')

    # posixAccount
    uid = fields.IntegerField(db_column='uidNumber', unique=True)
    group = fields.IntegerField(db_column='gidNumber')
    gecos = fields.CharField(db_column='gecos')
    home_directory = fields.CharField(db_column='homeDirectory')
    login_shell = fields.CharField(db_column='loginShell', default='/bin/bash')
    username = fields.CharField(db_column='uid')

    @property
    def organization(self):
        return self.org

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.full_name

class RCLdapGroup(ldapdb.models.Model):
    """
    Class for representing an LDAP group entry.
    """
    rdn_keys = ['name']

    # LDAP meta-data
    base_dn = "ou=groups,dc=example,dc=org"
    object_classes = ['posixGroup']

    # posixGroup attributes
    gid = fields.IntegerField(db_column='gidNumber', unique=True)
    name = fields.CharField(db_column='cn', max_length=200)
    members = fields.ListField(db_column='memberUid')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name




class LdapUser(ldapdb.models.Model):
    """
    Class for representing an LDAP user entry.
    """
    rdn_keys = ['username']

    # LDAP meta-data
    base_dn = "ou=people,dc=example,dc=org"
    object_classes = ['posixAccount', 'shadowAccount', 'inetOrgPerson']
    last_modified = fields.DateTimeField(db_column='modifyTimestamp')

    organization = fields.CharField(max_length=128,blank=False,null=False)

    # inetOrgPerson
    first_name = fields.CharField(db_column='givenName', verbose_name="Prime name")
    last_name = fields.CharField("Final name", db_column='sn')
    full_name = fields.CharField(db_column='cn')
    email = fields.CharField(db_column='mail')
    phone = fields.CharField(db_column='telephoneNumber', blank=True)
    mobile_phone = fields.CharField(db_column='mobile', blank=True)
    photo = fields.ImageField(db_column='jpegPhoto')

    # posixAccount
    uid = fields.IntegerField(db_column='uidNumber', unique=True)
    group = fields.IntegerField(db_column='gidNumber')
    gecos = fields.CharField(db_column='gecos')
    home_directory = fields.CharField(db_column='homeDirectory')
    login_shell = fields.CharField(db_column='loginShell', default='/bin/bash')
    username = fields.CharField(db_column='uid')
    password = fields.CharField(db_column='userPassword')

    # shadowAccount
    last_password_change = fields.TimestampField(db_column='shadowLastChange')

    @property
    def organization(self):
        return self.org

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.full_name


class LdapGroup(ldapdb.models.Model):
    """
    Class for representing an LDAP group entry.
    """
    rdn_keys = ['name']

    # LDAP meta-data
    base_dn = "ou=groups,dc=example,dc=org"
    object_classes = ['posixGroup']

    # posixGroup attributes
    gid = fields.IntegerField(db_column='gidNumber', unique=True)
    name = fields.CharField(db_column='cn', max_length=200)
    usernames = fields.ListField(db_column='memberUid')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class LdapMultiPKRoom(ldapdb.models.Model):
    """
    Class for representing a room, using a composite primary key.
    """
    rdn_keys = ['name', 'number']

    # LDAP meta-data
    base_dn = "ou=rooms,dc=example,dc=org"
    object_classes = ['room']

    # room attributes
    name = fields.CharField(db_column='cn', max_length=200)
    number = fields.CharField(db_column='roomNumber', max_length=10)
    phone = fields.CharField(db_column='telephoneNumber', max_length=20, blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.number)


class AbstractGroup(ldapdb.models.Model):
    class Meta:
        abstract = True

    rdn_keys = ['name']

    object_classes = ['posixGroup']
    gid = fields.IntegerField(db_column='gidNumber', unique=True)
    name = fields.CharField(db_column='cn', max_length=200)
    usernames = fields.ListField(db_column='memberUid')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ConcreteGroup(AbstractGroup):
    base_dn = "ou=groups,dc=example,dc=org"
