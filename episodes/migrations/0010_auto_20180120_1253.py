# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-20 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0009_auto_20180119_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['ep_number']},
        ),
    ]