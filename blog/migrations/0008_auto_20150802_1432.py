# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0007_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, verbose_name='Autor', null=True, to=settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL),
        ),
    ]
