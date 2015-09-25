# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Titel')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Homepage')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
            options={
                'verbose_name_plural': 'Links',
                'verbose_name': 'Link',
            },
        ),
        migrations.CreateModel(
            name='LinkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
            options={
                'verbose_name_plural': 'Kategorien',
                'verbose_name': 'Kategorie',
            },
        ),
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.ForeignKey(to='links.LinkCategory'),
        ),
    ]
