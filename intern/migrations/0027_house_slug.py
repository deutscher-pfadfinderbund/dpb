# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 07:17
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0026_auto_20160308_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name'),
        ),
    ]