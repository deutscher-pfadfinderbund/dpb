# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
import requests


class Date(models.Model):
    title = models.CharField('Titel', max_length=128, blank=False)
    start = models.DateTimeField('Beginn', blank=True)
    end = models.DateTimeField('Ende', blank=True)
    location = models.CharField('Ort', max_length=128, blank=True)
    latitude = models.FloatField('Breitengrad', max_length=128, blank=True, null=True)
    longitude = models.FloatField('Längengrad', max_length=128, blank=True, null=True)
    display_name = models.CharField('Berechneter Standort', max_length=128, blank=True, null=True)
    description = models.TextField('Beschreibung', blank=True)
    host = models.CharField('Ausrichter', max_length=128, blank=True)
    attachment = FilerFileField(verbose_name='Anhang', null=True, blank=True, related_name="date_attachment")
    created = models.DateTimeField('Erstellt am', default=datetime.now)

    def clean(self):
        try:
            data = requests.get("http://nominatim.openstreetmap.org/search?q=" + str(self.location) + "&format=json&polygon=1&addressdetails=1").json()[0]
            self.latitude = data["lat"]
            self.longitude = data["lon"]
            self.display_name = data["display_name"]
        except:
            self.latitude = None
            self.longitude = None
            self.display_name = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'


class House(models.Model):
    name = models.CharField('Name', max_length=128, blank=False)
    street = models.CharField('Straße', max_length=128, blank=False)
    plz = models.CharField('PLZ', max_length=128, blank=False)
    city = models.CharField('Stadt', max_length=128, blank=False)
    gmaps_location = models.URLField('Google Maps Link', blank=True, null=True)
    osm_location = models.URLField('OSM Link', blank=True, null=True)
    latitude = models.FloatField('Breitengrad', max_length=128, blank=True, null=True)
    longitude = models.FloatField('Längengrad', max_length=128, blank=True, null=True)
    display_name = models.CharField('Berechneter Standort', max_length=128, blank=True, null=True)
    website = models.URLField('Homepage', blank=True, null=True)
    image = FilerImageField(related_name="house_image", blank=True, null=True)
    owner = models.CharField('Name der Gruppe', max_length=128, blank=True, null=True)
    contact_name = models.CharField('Ansprechpartner', max_length=128, blank=False)
    contact_tel = models.CharField('Telefon', max_length=128, blank=False)
    contact_email = models.EmailField('E-Mail', max_length=128, blank=True, null=True)
    description = models.TextField('Beschreibung', blank=True, null=True)
    capacity_house = models.CharField('Schlafplätze im Haus', max_length=128, blank=True, null=True)
    capacity_outdoor = models.CharField('Schlafplätze außerhalb', max_length=128, blank=True, null=True)
    price_intern = models.CharField('Preise für Pfadfinder', max_length=128, blank=True, null=True)
    price_extern = models.CharField('Preise für Externe', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Haus'
        verbose_name_plural = 'Häuser'
