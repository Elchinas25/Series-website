# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-16 16:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20180115_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['-rating']},
        ),
    ]