# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0003_auto_20150910_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='date',
            options={'verbose_name_plural': 'Termine', 'verbose_name': 'Termin'},
        ),
        migrations.RemoveField(
            model_name='date',
            name='date',
        ),
        migrations.AddField(
            model_name='date',
            name='end',
            field=models.DateTimeField(verbose_name='Ende', default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='date',
            name='start',
            field=models.DateTimeField(verbose_name='Beginn', default=datetime.datetime.now, blank=True),
        ),
    ]
