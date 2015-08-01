# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_auto_20150726_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=filer.fields.file.FilerFileField(related_name='item_file', blank=True, to='filer.File', null=True, verbose_name='Datei'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='item_image', blank=True, to='filer.Image', null=True, verbose_name='Bild'),
        ),
    ]
