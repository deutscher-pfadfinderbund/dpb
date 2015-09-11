from django.db import models

from datetime import datetime


class Date(models.Model):
    title = models.CharField('Titel', max_length=128, blank=False)
    start = models.DateTimeField('Beginn', default=datetime.now, blank=True)
    end = models.DateTimeField('Ende', default=datetime.now, blank=True)
    location = models.CharField('Ort', max_length=128, blank=True)
    location_gmaps = models.URLField('Google Maps URL', blank=True)
    description = models.TextField('Beschreibung', blank=True)
    host = models.CharField('Ausrichter', max_length=128, blank=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'