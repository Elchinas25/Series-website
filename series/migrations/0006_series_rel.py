# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-21 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_series_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='rel',
            field=models.DateTimeField(null=True),
        ),
    ]
