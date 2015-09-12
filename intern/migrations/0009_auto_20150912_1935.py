# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0008_remove_date_location_gmaps'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='latitude',
            field=models.FloatField(max_length=128, verbose_name='Breitengrad', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='longitude',
            field=models.FloatField(max_length=128, verbose_name='Längengrad', blank=True, null=True),
        ),
    ]
