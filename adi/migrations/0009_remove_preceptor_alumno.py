# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-04 00:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0008_auto_20170804_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preceptor',
            name='alumno',
        ),
    ]
