# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0035_auto_20171116_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='codigo_como_firma',
            field=models.CharField(default='P24H2', max_length=5, unique=True, verbose_name='Firma'),
        ),
    ]
