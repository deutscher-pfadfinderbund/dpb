# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_auto_20150502_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='file',
        ),
        migrations.RemoveField(
            model_name='item',
            name='public',
        ),
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Aktivitätsstatus'),
        ),
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Anzahl / Exemplare', blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='collection',
            field=models.CharField(blank=True, verbose_name='Sammlungsteil', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='crossreference',
            field=models.CharField(blank=True, verbose_name='Querverweis', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.CharField(blank=True, verbose_name='Datum (Vorlage)', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='doctype',
            field=models.CharField(choices=[('Adressverzeichnis', 'Adressverzeichnis'), ('Chronik / Dokumentation', 'Chronik / Dokumentation'), ('Fahrtenbericht', 'Fahrtenbericht'), ('Kalender', 'Kalender'), ('Lagerheft', 'Lagerheft'), ('Lebensbericht', 'Lebensbericht'), ('Liederbuch', 'Liederbuch'), ('Ordnung', 'Ordnung'), ('Protokoll', 'Protokoll'), ('Reden', 'Reden'), ('Schöpferisches (Gedicht, Lieder, ...)', 'Schöpferisches (Gedicht, Lieder, ...)'), ('Schriftwechsel', 'Schriftwechsel'), ('Sonstiges', 'Sonstiges'), ('Zeitschrift', 'Zeitschrift'), ('Zeitungsartikel', 'Zeitungsartikel')], blank=True, verbose_name='Dokumenttyp', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='keywords',
            field=models.TextField(default='', verbose_name='Schlagworte *', max_length=1024),
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(blank=True, verbose_name='Standort (analoges Archiv)', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='medartanalog',
            field=models.CharField(choices=[('Buch', 'Buch'), ('CD / DVD', 'CD / DVD'), ('Dia(s)', 'Dia(s)'), ('Fahne / Wimpel', 'Fahne / Wimpel'), ('Filmspule', 'Filmspule'), ('Foto(s)', 'Foto(s)'), ('Gegenstand', 'Gegenstand'), ('Kassette', 'Kassette'), ('Schallplatte', 'Schallplatte'), ('Schrifttum', 'Schrifttum'), ('Sonstiges', 'Sonstiges'), ('Stempel', 'Stempel'), ('Tonband', 'Tonband'), ('VHS', 'VHS'), ('Wappen und Zeichen', 'Wappen und Zeichen')], blank=True, verbose_name='Medienart analog', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='medartdig',
            field=models.CharField(choices=[('Audiodatei', 'Audiodatei'), ('Buch', 'Buch'), ('Foto(s)', 'Foto(s)'), ('Schrifttum', 'Schrifttum'), ('Sonstiges', 'Sonstiges'), ('Videodatei', 'Videodatei')], blank=True, verbose_name='Medienart digital', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Anmerkungen', max_length=1024),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.CharField(blank=True, verbose_name='Besitzer', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.CharField(blank=True, verbose_name='Ort / Veröffentlichung', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='reviewed',
            field=models.BooleanField(default=True, verbose_name='Bearbeitungsstatus'),
        ),
        migrations.AddField(
            model_name='item',
            name='source',
            field=models.CharField(blank=True, verbose_name='Quelle', max_length=256),
        ),
        migrations.AddField(
            model_name='item',
            name='year',
            field=models.IntegerField(default='1900', verbose_name='Jahr', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(blank=True, verbose_name='Autor', max_length=256),
        ),
        migrations.AlterField(
            model_name='item',
            name='signature',
            field=models.CharField(blank=True, verbose_name='Signatur', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(verbose_name='Titel *', max_length=256),
        ),
    ]
