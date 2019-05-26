# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import filer.fields.file
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('intern', '0006_date_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='attachment',
            field=filer.fields.file.FilerFileField(related_name='date_attachment', verbose_name='Anhang', null=True,
                                                   blank=True, to='filer.File', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='date',
            name='end',
            field=models.DateTimeField(verbose_name='Ende', blank=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='start',
            field=models.DateTimeField(verbose_name='Beginn', blank=True),
        ),
    ]
