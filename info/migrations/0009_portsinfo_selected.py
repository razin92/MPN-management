# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_switch_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='portsinfo',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
