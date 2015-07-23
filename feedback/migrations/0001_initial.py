# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', blank=True, default='Anonym', max_length=50)),
                ('note', models.TextField(verbose_name='Anmerkung', max_length=1024)),
                ('created', models.DateTimeField(verbose_name='Erstellt am', default=datetime.datetime.now)),
            ],
        ),
    ]
