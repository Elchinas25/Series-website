# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-17 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0005_auto_20180117_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
