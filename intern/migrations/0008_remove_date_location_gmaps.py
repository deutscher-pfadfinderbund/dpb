# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0007_auto_20150911_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='location_gmaps',
        ),
    ]
