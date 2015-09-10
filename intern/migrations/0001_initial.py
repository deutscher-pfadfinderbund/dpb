# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Titel')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Datum')),
                ('location', models.CharField(max_length=128, verbose_name='Ort')),
                ('location_gmaps', models.URLField(verbose_name='Google Maps URL')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('host', models.CharField(max_length=128, verbose_name='Ausrichter')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
        ),
    ]
