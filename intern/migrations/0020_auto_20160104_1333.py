# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0019_auto_20160104_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='accessibility',
            field=models.CharField(max_length=1024, null=True, verbose_name='Erreichbarkeit', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='capacity_house',
            field=models.CharField(max_length=1024, null=True, verbose_name='Schlafplätze im Haus', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='capacity_outdoor',
            field=models.CharField(max_length=1024, null=True, verbose_name='Schlafplätze außerhalb', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Stadt'),
        ),
        migrations.AlterField(
            model_name='house',
            name='contact_email',
            field=models.EmailField(max_length=1024, null=True, verbose_name='E-Mail', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='contact_name',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Ansprechpartner'),
        ),
        migrations.AlterField(
            model_name='house',
            name='contact_tel',
            field=models.CharField(max_length=1024, null=True, verbose_name='Telefon', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='display_name',
            field=models.CharField(max_length=1024, null=True, verbose_name='Berechneter Standort', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='latitude',
            field=models.FloatField(max_length=1024, null=True, verbose_name='Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='longitude',
            field=models.FloatField(max_length=1024, null=True, verbose_name='Längengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.CharField(max_length=1024, null=True, verbose_name='Name der Gruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='plz',
            field=models.CharField(blank=True, max_length=1024, verbose_name='PLZ'),
        ),
        migrations.AlterField(
            model_name='house',
            name='price_extern',
            field=models.CharField(max_length=1024, null=True, verbose_name='Preise für Externe', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='price_intern',
            field=models.CharField(max_length=1024, null=True, verbose_name='Preise für Pfadfinder', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='situation',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Lage'),
        ),
        migrations.AlterField(
            model_name='house',
            name='state',
            field=models.CharField(max_length=1024, null=True, verbose_name='Bundesland', blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Straße'),
        ),
    ]
