# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_auto_20150910_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Datum', blank=True),
        ),
    ]
