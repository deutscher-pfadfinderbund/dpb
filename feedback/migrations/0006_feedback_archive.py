# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_feedback_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='Bearbeitet?'),
        ),
    ]
