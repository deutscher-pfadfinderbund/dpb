# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0013_house_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='accessibility',
            field=models.CharField(max_length=128, null=True, verbose_name='Erreichbarkeit', blank=True),
        ),
        migrations.AddField(
            model_name='house',
            name='state',
            field=models.CharField(max_length=128, null=True, verbose_name='Bundesland', blank=True),
        ),
    ]
