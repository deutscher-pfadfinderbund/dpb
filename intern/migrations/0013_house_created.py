# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0012_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='created',
            field=models.DateTimeField(verbose_name='Erstellt am', default=datetime.datetime.now),
        ),
    ]
