# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20150502_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(default=None, upload_to='archive', verbose_name='Datei hochladen'),
        ),
    ]
