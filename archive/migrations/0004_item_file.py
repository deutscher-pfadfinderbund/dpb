# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_item_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file',
            field=models.FileField(upload_to='', default=False),
        ),
    ]
