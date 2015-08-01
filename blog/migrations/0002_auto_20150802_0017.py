# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategorien', 'verbose_name': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created',), 'verbose_name_plural': 'Beiträge', 'verbose_name': 'Beitrag'},
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Kategorien'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Inhalt'),
        ),
    ]
