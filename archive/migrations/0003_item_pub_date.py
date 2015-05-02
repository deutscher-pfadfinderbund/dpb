# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20150502_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 2, 12, 29, 10, 200833, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
