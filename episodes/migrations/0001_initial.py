# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-16 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateField(auto_now=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
