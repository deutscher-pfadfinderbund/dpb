from datetime import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField('Titel', max_length=50, blank=False)
    content = models.TextField('Inhalt', max_length=1024, blank=False)
    archive = models.BooleanField('Archiviert?', default=False)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)


class Category(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)