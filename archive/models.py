# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from filer.fields.file import FilerFileField


class Year(models.Model):
    year = models.IntegerField("Jahr", blank=False)
    created = models.DateTimeField("Erstellt am", default=timezone.now)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Jahr"
        verbose_name_plural = "Jahre"
        ordering = ['year', ]


class Item(models.Model):
    # Define Choices
    doctype_choices = (
        ("Adressverzeichnis", "Adressverzeichnis"),
        ("Chronik / Dokumentation", "Chronik / Dokumentation"),
        ("Fahrtenbericht", "Fahrtenbericht"),
        ("Kalender", "Kalender"),
        ("Lagerheft", "Lagerheft"),
        ("Lebensbericht", "Lebensbericht"),
        ("Liederbuch", "Liederbuch"),
        ("Ordnung", "Ordnung"),
        ("Protokoll", "Protokoll"),
        ("Reden", "Reden"),
        ("Schöpferisches (Gedicht, Lieder, ...)", "Schöpferisches (Gedicht, Lieder, ...)"),
        ("Schriftwechsel", "Schriftwechsel"),
        ("Sonstiges", "Sonstiges"),
        ("Zeitschrift", "Zeitschrift"),
        ("Zeitungsartikel", "Zeitungsartikel"),
    )
    medartanalog_choices = (
        ("Audiodatei", "Audiodatei"),
        ("Buch", "Buch"),
        ("CD / DVD", "CD / DVD"),
        ("Dia(s)", "Dia(s)"),
        ("Fahne / Wimpel", "Fahne / Wimpel"),
        ("Filmspule", "Filmspule"),
        ("Foto(s)", "Foto(s)"),
        ("Gegenstand", "Gegenstand"),
        ("Kassette", "Kassette"),
        ("Schallplatte", "Schallplatte"),
        ("Schrifttum", "Schrifttum"),
        ("Sonstiges", "Sonstiges"),
        ("Stempel", "Stempel"),
        ("Tonband", "Tonband"),
        ("VHS", "VHS"),
        ("Videodatei", "Videodatei"),
        ("Wappen und Zeichen", "Wappen und Zeichen"),
    )
    collection_choices = (
        ("Bund", "Bund"),
        ("DPB vor 1945", "DPB vor 1945"),
        ("Jungenbund", "Jungenbund"),
        ("Mädchenbund", "Mädchenbund"),
        ("Orden St. Georg", "Orden St. Georg"),
        ("Orden St. Christophorus", "Orden St. Christophorus"),
        ("Gruppen des DPB", "Gruppen des DPB"),
        ("Überbündisches", "Überbündisches"),
    )

    signature = models.CharField('Signatur', max_length=50, blank=True)
    author = models.CharField('Autor', max_length=256, blank=True)
    title = models.CharField('Titel *', max_length=256)
    date = models.CharField('Datum (Vorlage)', max_length=256, blank=True)
    year = models.IntegerField('Jahr', null=True, blank=True)
    place = models.CharField('Ort / Veröffentlichung', max_length=256, blank=True)
    medartanalog = models.CharField('Medienart *', max_length=256, choices=medartanalog_choices, blank=False)
    doctype = models.CharField('Dokumenttyp', max_length=256, choices=doctype_choices, blank=True)

    file = FilerFileField(null=True, blank=True, related_name="item_file", verbose_name='Datei',
                          on_delete=models.CASCADE)
    file2 = FilerFileField(null=True, blank=True, related_name="item_file2", verbose_name='Datei 2',
                           on_delete=models.CASCADE)
    file3 = FilerFileField(null=True, blank=True, related_name="item_file3", verbose_name='Datei 3',
                           on_delete=models.CASCADE)

    keywords = models.TextField('Schlagworte *', default="", max_length=1024)
    location = models.CharField('Standort (analoges Archiv)', max_length=256, blank=True)
    source = models.CharField('Quelle', max_length=256, blank=True)
    notes = models.TextField('Anmerkungen', max_length=1024, blank=True)
    collection = models.CharField('Sammlungsteil *', max_length=256, choices=collection_choices, blank=False)
    amount = models.IntegerField('Anzahl / Exemplare', default=1, null=True, blank=True)
    crossreference = models.CharField('Querverweis', max_length=256, blank=True)
    active = models.BooleanField('Öffentlich? (intern)', default=True)
    reviewed = models.BooleanField('Bearbeitet?', default=True)
    owner = models.CharField('Besitzer', max_length=256, blank=True)
    pub_date = models.DateTimeField('Hinzugefügt am', default=timezone.now)
    modified = models.DateTimeField('Zuletzt geändert', auto_now=True)

    def __str__(self):
        return str(self.signature) + " - " + self.title

    def has_file(self):
        return self.file is not None

    has_file.boolean = True
    has_file.short_description = "Digital?"


class Feedback(models.Model):
    name = models.CharField('Name *', max_length=128, blank=False)
    email = models.EmailField('E-Mail *', max_length=255, blank=False)
    group = models.CharField('Gruppierung', max_length=1024, blank=True)
    note = models.TextField('Anmerkung *', max_length=1024, blank=False)
    archive = models.BooleanField('Bearbeitet?', default=False)
    item = models.ForeignKey(Item, verbose_name="Bezieht sich auf", blank=False, on_delete=models.SET_NULL)
    created = models.DateTimeField('Erstellt am', default=timezone.now)
    modified = models.DateTimeField('Zuletzt geändert', auto_now=True)

    def __str__(self):
        return self.name
