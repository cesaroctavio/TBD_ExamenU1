# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='studio',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, default='Year', max_length=120, null=True),
        ),
    ]
