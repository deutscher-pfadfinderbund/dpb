# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0028_auto_20160310_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='rooms_other',
            field=models.TextField(blank=True, max_length=4096, verbose_name='Sonstiges zu den Räumen'),
        ),
    ]