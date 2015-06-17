# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('enable_comments', models.BooleanField(verbose_name='enable comments', default=False)),
                ('template_name', models.CharField(max_length=70, blank=True, verbose_name='template name', help_text="Example: 'pages/contact_page.html'. If this isn't provided, the system will use 'pages/default.html'.")),
                ('registration_required', models.BooleanField(verbose_name='registration required', help_text='If this is checked, only logged-in users will be able to view the page.', default=False)),
                ('attachment', filer.fields.file.FilerFileField(null=True, related_name='attachment', blank=True, to='filer.File')),
                ('image', filer.fields.image.FilerImageField(null=True, related_name='image', blank=True, to='filer.Image')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'verbose_name': 'page',
                'db_table': 'pages',
                'verbose_name_plural': 'pages',
                'ordering': ('url',),
            },
        ),
    ]
