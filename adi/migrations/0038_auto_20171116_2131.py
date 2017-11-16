# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adi', '0037_auto_20171116_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='grupo_usuario',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='nombre_usuario',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardia',
            name='grupo_usuario',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guardia',
            name='nombre_usuario',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='grupo_usuario',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='nombre_usuario',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='codigo_como_firma',
            field=models.CharField(default='MBATB', max_length=5, unique=True, verbose_name='Firma'),
        ),
    ]
