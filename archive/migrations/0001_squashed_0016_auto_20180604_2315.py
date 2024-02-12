# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 11:54
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
import filer.fields.file
from django.db import migrations, models
from datetime import timezone


class Migration(migrations.Migration):
    replaces = [('archive', '0001_initial'), ('archive', '0002_auto_20150502_1204'), ('archive', '0003_item_pub_date'),
                ('archive', '0004_item_file'), ('archive', '0005_auto_20150502_1459'),
                ('archive', '0006_auto_20150502_1848'), ('archive', '0007_auto_20150502_1857'),
                ('archive', '0008_auto_20150502_1858'), ('archive', '0009_auto_20150502_2329'),
                ('archive', '0010_auto_20150502_2331'), ('archive', '0011_auto_20150502_2357'),
                ('archive', '0012_auto_20150726_2046'), ('archive', '0013_auto_20150728_1923'),
                ('archive', '0014_auto_20160814_2117'), ('archive', '0015_auto_20180418_1043'),
                ('archive', '0016_auto_20180604_2315')]

    initial = True

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(blank=True, max_length=50, verbose_name='Signatur')),
                ('author', models.CharField(blank=True, max_length=256, verbose_name='Autor')),
                ('title', models.CharField(max_length=256, verbose_name='Titel *')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Hinzugefügt am')),
                ('active', models.BooleanField(default=False, verbose_name='Öffentlich? (intern)')),
                ('amount', models.IntegerField(blank=True, default=1, null=True, verbose_name='Anzahl / Exemplare')),
                ('collection', models.CharField(
                    choices=[('Bund', 'Bund'), ('DPB vor 1945', 'DPB vor 1945'), ('Jungenbund', 'Jungenbund'),
                             ('Mädchenbund', 'Mädchenbund'), ('Orden St.Georg', 'Orden St.Georg'),
                             ('Orden St.Christophorus', 'Orden St.Christophorus'),
                             ('Gruppen des DPB', 'Gruppen des DPB'), ('Überbündisches', 'Überbündisches')],
                    max_length=256, verbose_name='Sammlungsteil *')),
                ('crossreference', models.CharField(blank=True, max_length=256, verbose_name='Querverweis')),
                ('date', models.CharField(blank=True, max_length=256, verbose_name='Datum (Vorlage)')),
                ('doctype', models.CharField(blank=True, choices=[('Adressverzeichnis', 'Adressverzeichnis'), (
                    'Chronik / Dokumentation', 'Chronik / Dokumentation'), ('Fahrtenbericht', 'Fahrtenbericht'),
                                                                  ('Kalender', 'Kalender'), ('Lagerheft', 'Lagerheft'),
                                                                  ('Lebensbericht', 'Lebensbericht'),
                                                                  ('Liederbuch', 'Liederbuch'), ('Ordnung', 'Ordnung'),
                                                                  ('Protokoll', 'Protokoll'), ('Reden', 'Reden'), (
                                                                      'Schöpferisches (Gedicht, Lieder, ...)',
                                                                      'Schöpferisches (Gedicht, Lieder, ...)'),
                                                                  ('Schriftwechsel', 'Schriftwechsel'),
                                                                  ('Sonstiges', 'Sonstiges'),
                                                                  ('Zeitschrift', 'Zeitschrift'),
                                                                  ('Zeitungsartikel', 'Zeitungsartikel')],
                                             max_length=256, verbose_name='Dokumenttyp')),
                ('keywords', models.TextField(default='', max_length=1024, verbose_name='Schlagworte *')),
                ('location', models.CharField(blank=True, max_length=256, verbose_name='Standort (analoges Archiv)')),
                ('medartanalog', models.CharField(
                    choices=[('Audiodatei', 'Audiodatei'), ('Buch', 'Buch'), ('CD / DVD', 'CD / DVD'),
                             ('Dia(s)', 'Dia(s)'), ('Fahne / Wimpel', 'Fahne / Wimpel'), ('Filmspule', 'Filmspule'),
                             ('Foto(s)', 'Foto(s)'), ('Gegenstand', 'Gegenstand'), ('Kassette', 'Kassette'),
                             ('Schallplatte', 'Schallplatte'), ('Schrifttum', 'Schrifttum'), ('Sonstiges', 'Sonstiges'),
                             ('Stempel', 'Stempel'), ('Tonband', 'Tonband'), ('VHS', 'VHS'),
                             ('Videodatei', 'Videodatei'), ('Wappen und Zeichen', 'Wappen und Zeichen')],
                    max_length=256, verbose_name='Medienart *')),
                ('notes', models.TextField(blank=True, max_length=1024, verbose_name='Anmerkungen')),
                ('owner', models.CharField(blank=True, max_length=256, verbose_name='Besitzer')),
                ('place', models.CharField(blank=True, max_length=256, verbose_name='Ort / Veröffentlichung')),
                ('reviewed', models.BooleanField(default=True, verbose_name='Bearbeitet?')),
                ('source', models.CharField(blank=True, max_length=256, verbose_name='Quelle')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Jahr')),
                ('file',
                 filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='item_file', to='filer.File', verbose_name='Datei')),
                ('modified', models.DateTimeField(auto_now=True,
                                                  default=datetime.datetime(2016, 8, 14, 19, 17, 55, 636364,
                                                                            tzinfo=timezone.utc),
                                                  verbose_name='Zuletzt geändert')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name *')),
                ('email', models.EmailField(max_length=255, verbose_name='E-Mail *')),
                ('group', models.CharField(blank=True, max_length=1024, verbose_name='Gruppierung')),
                ('note', models.TextField(max_length=1024, verbose_name='Anmerkung *')),
                ('archive', models.BooleanField(default=False, verbose_name='Bearbeitet?')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Zuletzt geändert')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Item',
                                           verbose_name='Bezieht sich auf')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Jahr')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Erstellt am')),
            ],
            options={
                'ordering': ['year'],
                'verbose_name_plural': 'Jahre',
                'verbose_name': 'Jahr',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='years',
            field=models.ManyToManyField(blank=True, to='archive.Year', verbose_name='Jahre'),
        ),
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Öffentlich? (intern)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='collection',
            field=models.CharField(
                choices=[('Bund', 'Bund'), ('DPB vor 1945', 'DPB vor 1945'), ('Jungenbund', 'Jungenbund'),
                         ('Mädchenbund', 'Mädchenbund'), ('Orden St. Georg', 'Orden St. Georg'),
                         ('Orden St. Christophorus', 'Orden St. Christophorus'), ('Gruppen des DPB', 'Gruppen des DPB'),
                         ('Überbündisches', 'Überbündisches')], max_length=256, verbose_name='Sammlungsteil *'),
        ),
        migrations.AddField(
            model_name='item',
            name='file2',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='item_file2', to='filer.File', verbose_name='Datei 2'),
        ),
        migrations.AddField(
            model_name='item',
            name='file3',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                   related_name='item_file3', to='filer.File', verbose_name='Datei 3'),
        ),
    ]
