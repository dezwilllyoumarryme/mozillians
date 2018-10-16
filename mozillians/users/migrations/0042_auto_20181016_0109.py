# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-16 08:09
from __future__ import unicode_literals

from django.db import migrations


def delete_mozilla_location_external_account(apps, schema_editor):
    ExternalAccount = apps.get_model('users', 'ExternalAccount')
    ExternalAccount.objects.filter(type='MOZILLALOCATION').delete()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20181009_0207'),
    ]

    operations = [
        migrations.RunPython(delete_mozilla_location_external_account, backwards),
    ]
