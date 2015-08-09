# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150802_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='intro',
            field=models.TextField(verbose_name='Kurzbeschreibung', null=True, blank=True),
        ),
    ]
