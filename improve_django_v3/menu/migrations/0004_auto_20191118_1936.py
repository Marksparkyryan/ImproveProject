# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-11-19 03:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20191118_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='expiration_date',
        ),
    ]
