# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 07:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from datetime import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0024_auto_20160306_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 7, 7, 33, 58, 97313, tzinfo=timezone.utc), verbose_name='Zuletzt geändert'),
            preserve_default=False,
        ),
    ]
