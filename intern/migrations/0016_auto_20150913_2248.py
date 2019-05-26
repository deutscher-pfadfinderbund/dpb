# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import filer.fields.image
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('intern', '0015_auto_20150913_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image1',
            field=filer.fields.image.FilerImageField(related_name='house_image1', to='filer.Image', null=True,
                                                     blank=True, verbose_name='1. Bild', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='house',
            name='image2',
            field=filer.fields.image.FilerImageField(related_name='house_image2', to='filer.Image', null=True,
                                                     blank=True, verbose_name='2. Bild', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='house',
            name='image3',
            field=filer.fields.image.FilerImageField(related_name='house_image3', to='filer.Image', null=True,
                                                     blank=True, verbose_name='3. Bild', on_delete=models.CASCADE),
        ),
    ]
