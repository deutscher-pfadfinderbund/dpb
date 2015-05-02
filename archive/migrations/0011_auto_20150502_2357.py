# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_auto_20150502_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.IntegerField(blank=True, verbose_name='Anzahl / Exemplare', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='year',
            field=models.IntegerField(blank=True, verbose_name='Jahr', null=True),
        ),
    ]
