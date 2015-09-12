from django.db import models

from datetime import datetime
from filer.fields.file import FilerFileField


class Date(models.Model):
    title = models.CharField('Titel', max_length=128, blank=False)
    start = models.DateTimeField('Beginn', blank=True)
    end = models.DateTimeField('Ende', blank=True)
    location = models.CharField('Ort', max_length=128, blank=True)
    description = models.TextField('Beschreibung', blank=True)
    host = models.CharField('Ausrichter', max_length=128, blank=True)
    attachment = FilerFileField(verbose_name='Anhang', null=True, blank=True, related_name="date_attachment")
    created = models.DateTimeField('Erstellt am', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'