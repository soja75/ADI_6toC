# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adi', '0034_auto_20171116_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='preceptor',
            name='nombre_usuario',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='codigo_como_firma',
            field=models.CharField(default='YSEI2', max_length=5, unique=True, verbose_name='Firma'),
        ),
    ]