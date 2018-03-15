from autoslug import AutoSlugField
from django.db import models


class Document(models.Model):
    title = models.CharField("Titel", max_length=256, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField("Beschreibung", blank=True, null=True)
    file = models.FileField(upload_to='maedchenbund', verbose_name='Datei', blank=False, null=False)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dokument"
        verbose_name_plural = "Dokumente"
