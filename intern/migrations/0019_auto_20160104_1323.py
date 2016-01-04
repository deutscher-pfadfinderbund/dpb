# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0018_delete_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='situation',
            field=models.CharField(verbose_name='Lage', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(verbose_name='Stadt', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='contact_name',
            field=models.CharField(verbose_name='Ansprechpartner', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='plz',
            field=models.CharField(verbose_name='PLZ', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.CharField(verbose_name='Straße', max_length=128, blank=True),
        ),
    ]
