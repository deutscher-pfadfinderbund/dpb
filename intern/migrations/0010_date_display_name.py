# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0009_auto_20150912_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='display_name',
            field=models.CharField(verbose_name='Berechneter Standort', max_length=128, blank=True),
        ),
    ]
