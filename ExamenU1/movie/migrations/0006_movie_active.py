# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
