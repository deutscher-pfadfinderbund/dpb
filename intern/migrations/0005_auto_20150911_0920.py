# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0004_auto_20150911_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='description',
            field=models.TextField(blank=True, verbose_name='Beschreibung'),
        ),
    ]
