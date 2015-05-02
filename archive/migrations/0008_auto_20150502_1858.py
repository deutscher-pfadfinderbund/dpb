# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_auto_20150502_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, upload_to='archive', verbose_name='Datei hochladen'),
        ),
    ]
