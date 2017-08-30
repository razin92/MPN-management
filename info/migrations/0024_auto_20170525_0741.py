# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0023_auto_20170428_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='bill_url',
            field=models.URLField(blank=True, default='#', null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='login',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='telephone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
