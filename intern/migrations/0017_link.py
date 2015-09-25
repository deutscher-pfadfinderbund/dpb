# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0016_auto_20150913_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Titel', max_length=128)),
                ('website', models.URLField(verbose_name='Homepage', blank=True, null=True)),
                ('description', models.TextField(verbose_name='Beschreibung', blank=True)),
                ('created', models.DateTimeField(verbose_name='Erstellt am', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
