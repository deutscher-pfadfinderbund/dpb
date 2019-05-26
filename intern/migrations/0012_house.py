# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import filer.fields.image
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('intern', '0011_auto_20150912_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=128)),
                ('street', models.CharField(verbose_name='Straße', max_length=128)),
                ('plz', models.CharField(verbose_name='PLZ', max_length=128)),
                ('city', models.CharField(verbose_name='Stadt', max_length=128)),
                ('gmaps_location', models.URLField(null=True, blank=True, verbose_name='Google Maps Link')),
                ('osm_location', models.URLField(null=True, blank=True, verbose_name='OSM Link')),
                ('latitude', models.FloatField(null=True, blank=True, verbose_name='Breitengrad', max_length=128)),
                ('longitude', models.FloatField(null=True, blank=True, verbose_name='Längengrad', max_length=128)),
                ('display_name',
                 models.CharField(null=True, blank=True, verbose_name='Berechneter Standort', max_length=128)),
                ('website', models.URLField(null=True, blank=True, verbose_name='Homepage')),
                ('owner', models.CharField(null=True, blank=True, verbose_name='Name der Gruppe', max_length=128)),
                ('contact_name', models.CharField(verbose_name='Ansprechpartner', max_length=128)),
                ('contact_tel', models.CharField(verbose_name='Telefon', max_length=128)),
                ('contact_email', models.EmailField(null=True, blank=True, verbose_name='E-Mail', max_length=128)),
                ('description', models.TextField(null=True, blank=True, verbose_name='Beschreibung')),
                ('capacity_house',
                 models.CharField(null=True, blank=True, verbose_name='Schlafplätze im Haus', max_length=128)),
                ('capacity_outdoor',
                 models.CharField(null=True, blank=True, verbose_name='Schlafplätze außerhalb', max_length=128)),
                ('price_intern',
                 models.CharField(null=True, blank=True, verbose_name='Preise für Pfadfinder', max_length=128)),
                ('price_extern',
                 models.CharField(null=True, blank=True, verbose_name='Preise für Externe', max_length=128)),
                ('image',
                 filer.fields.image.FilerImageField(blank=True, null=True, related_name='house_image', to='filer.Image',
                                                    on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Häuser',
                'verbose_name': 'Haus',
            },
        ),
    ]
