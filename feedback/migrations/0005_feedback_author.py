# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.CharField(blank=True, default='Admin', verbose_name='Antwort von', max_length=50),
        ),
    ]
