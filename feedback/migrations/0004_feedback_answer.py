# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='answer',
            field=models.TextField(verbose_name='Antwort', blank=True, max_length=1024),
        ),
    ]
