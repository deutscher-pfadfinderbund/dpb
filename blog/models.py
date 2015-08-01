from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'


class Post(models.Model):
    title = models.CharField('Titel', max_length=50, blank=False)
    content = models.TextField('Inhalt', blank=False)
    archive = models.BooleanField('Archiviert?', default=False)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)
    categories = models.ManyToManyField(Category, verbose_name="Kategorien")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Beitrag'
        verbose_name_plural = 'Beiträge'
        ordering = ('created',)