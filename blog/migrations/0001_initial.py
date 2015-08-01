# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Titel')),
                ('content', models.TextField(max_length=1024, verbose_name='Inhalt')),
                ('archive', models.BooleanField(default=False, verbose_name='Archiviert?')),
                ('public', models.BooleanField(default=True, verbose_name='Öffentlich?')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
                ('categories', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]
