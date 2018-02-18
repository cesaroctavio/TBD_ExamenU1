# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('seleccionar', 'Seleccionar'), ('accion', 'Accion'), ('comedia', 'Comedia'), ('terror', 'Terror')], default='seleccionar', max_length=120),
        ),
    ]
