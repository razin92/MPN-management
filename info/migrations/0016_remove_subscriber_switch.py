# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20170421_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='switch',
        ),
    ]
