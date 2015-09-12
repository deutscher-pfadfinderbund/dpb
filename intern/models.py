# -*- coding: utf-8 -*-
from django.db import models

from datetime import datetime
from filer.fields.file import FilerFileField
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