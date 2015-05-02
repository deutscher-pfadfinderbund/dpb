# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20150502_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='public',
            field=models.BooleanField(verbose_name='Öffentlich?', default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(max_length=256, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(verbose_name='Datei hochladen', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Hinzugefügt am', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='signature',
            field=models.CharField(max_length=256, verbose_name='Signatur'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Titel'),
        ),
    ]
