# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
    ]
