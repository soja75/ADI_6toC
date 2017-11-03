# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-15 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0014_auto_20170814_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario2',
            name='apellido_alumno',
        ),
        migrations.RemoveField(
            model_name='formulario2',
            name='dni_alumno',
        ),
        migrations.RemoveField(
            model_name='formulario2',
            name='nombre_alumno',
        ),
        migrations.AddField(
            model_name='formulario2',
            name='alumnos',
            field=models.ForeignKey(default=132, on_delete=django.db.models.deletion.CASCADE, to='adi.Alumno'),
            preserve_default=False,
        ),
    ]
