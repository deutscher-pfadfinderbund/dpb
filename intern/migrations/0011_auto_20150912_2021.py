# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0010_date_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='display_name',
            field=models.CharField(max_length=128, verbose_name='Berechneter Standort', blank=True, null=True),
        ),
    ]
