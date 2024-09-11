from datetime import datetime

from django.db import models

from intern.models import State


class LinkCategory(models.Model):
    name = models.CharField('Name', max_length=128, blank=False)
    created = models.DateTimeField('Erstellt am', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'


class Link(models.Model):
    """ Links to the different groups in the DPB """
    title = models.CharField('Titel', max_length=128, blank=False)
    website = models.URLField('Homepage', blank=True, null=True)
    category = models.ForeignKey(LinkCategory, null=True, on_delete=models.SET_NULL)
    description = models.TextField('Beschreibung', blank=True)
    city = models.CharField('Stadt', max_length=1024, default="", blank=True)
    state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
