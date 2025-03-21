# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0017_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Link',
        ),
    ]
