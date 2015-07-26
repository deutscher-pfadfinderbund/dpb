# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('archive', '0011_auto_20150502_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file',
            field=filer.fields.file.FilerFileField(null=True, to='filer.File', blank=True, related_name='item_file'),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, to='filer.Image', blank=True, related_name='item_image'),
        ),
    ]
