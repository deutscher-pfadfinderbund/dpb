# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='public',
            field=models.BooleanField(verbose_name='Öffentlich?', default=True),
        ),
    ]
