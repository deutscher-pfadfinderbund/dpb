# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='host',
            field=models.CharField(blank=True, max_length=128, verbose_name='Ausrichter'),
        ),
        migrations.AlterField(
            model_name='date',
            name='location',
            field=models.CharField(blank=True, max_length=128, verbose_name='Ort'),
        ),
        migrations.AlterField(
            model_name='date',
            name='location_gmaps',
            field=models.URLField(blank=True, verbose_name='Google Maps URL'),
        ),
    ]
