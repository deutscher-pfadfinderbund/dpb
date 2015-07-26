# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

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
    medartdig_choices = (
        ("Audiodatei", "Audiodatei"),
        ("Buch", "Buch"),
        ("Foto(s)", "Foto(s)"),
        ("Schrifttum", "Schrifttum"),
        ("Sonstiges", "Sonstiges"),
        ("Videodatei", "Videodatei"),
    )
    medartanalog_choices = (
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
        ("Wappen und Zeichen", "Wappen und Zeichen"),
    )

    signature = models.CharField('Signatur', max_length=50, blank=True)
    author = models.CharField('Autor', max_length=256, blank=True)
    title = models.CharField('Titel *', max_length=256)
    date = models.CharField('Datum (Vorlage)', max_length=256, blank=True)
    year = models.IntegerField('Jahr', null=True, blank=True)
    place = models.CharField('Ort / Veröffentlichung', max_length=256, blank=True)
    medartdig = models.CharField('Medienart digital', max_length=256, choices=medartdig_choices, blank=True)
    medartanalog = models.CharField('Medienart analog', max_length=256, choices=medartanalog_choices, blank=True)
    doctype = models.CharField('Dokumenttyp', max_length=256, choices=doctype_choices, blank=True)
    keywords = models.TextField('Schlagworte *', default="", max_length=1024)
    location = models.CharField('Standort (analoges Archiv)', max_length=256, blank=True)
    source = models.CharField('Quelle', max_length=256, blank=True)
    notes = models.TextField('Anmerkungen', max_length=1024, blank=True)
    collection = models.CharField('Sammlungsteil', max_length=256, blank=True)
    amount = models.IntegerField('Anzahl / Exemplare', null=True, blank=True)
    crossreference = models.CharField('Querverweis', max_length=256, blank=True)
    active = models.BooleanField('Aktivitätsstatus', default=False)
    reviewed = models.BooleanField('Bearbeitungsstatus', default=True)
    owner = models.CharField('Besitzer', max_length=256, blank=True)
    pub_date = models.DateTimeField('Hinzugefügt am', default=datetime.now)

    def __str__(self):
        return self.title
