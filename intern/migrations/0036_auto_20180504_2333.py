# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-04 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('intern', '0035_auto_20160320_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='display_name',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Berechneter Standort'),
        ),
    ]
