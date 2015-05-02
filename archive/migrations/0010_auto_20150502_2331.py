# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20150502_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='year',
            field=models.IntegerField(default='0', blank=True, verbose_name='Jahr'),
        ),
    ]
