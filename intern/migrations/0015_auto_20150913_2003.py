# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('intern', '0014_auto_20150913_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='image',
        ),
        migrations.AddField(
            model_name='house',
            name='image1',
            field=filer.fields.image.FilerImageField(related_name='house_image1', blank=True, null=True, to='filer.Image'),
        ),
        migrations.AddField(
            model_name='house',
            name='image2',
            field=filer.fields.image.FilerImageField(related_name='house_image2', blank=True, null=True, to='filer.Image'),
        ),
        migrations.AddField(
            model_name='house',
            name='image3',
            field=filer.fields.image.FilerImageField(related_name='house_image3', blank=True, null=True, to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='house',
            name='contact_tel',
            field=models.CharField(max_length=128, blank=True, verbose_name='Telefon', null=True),
        ),
    ]
