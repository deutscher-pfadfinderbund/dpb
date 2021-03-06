# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0022_auto_20160306_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='sleep_outdoor',
            field=models.TextField(blank=True, max_length=4096, verbose_name='Schlafplätze auf dem Gelände'),
        ),
        migrations.AlterField(
            model_name='house',
            name='sleep_mattresses',
            field=models.IntegerField(blank=True, null=True, verbose_name='Anzahl der Matratzen'),
        ),
    ]
