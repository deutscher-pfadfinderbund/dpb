# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 18:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0020_auto_20160104_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
            options={
                'verbose_name_plural': 'Bundesländer',
                'verbose_name': 'Bundesland',
            },
        ),
    ]