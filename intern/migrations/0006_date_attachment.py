# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('intern', '0005_auto_20150911_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='attachment',
            field=filer.fields.file.FilerFileField(to='filer.File', null=True, related_name='Anhang', blank=True),
        ),
    ]
