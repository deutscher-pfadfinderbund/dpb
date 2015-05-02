from django.db import models
from datetime import datetime

class Item(models.Model):
    signature = models.CharField('Signatur', max_length=256)
    author = models.CharField('Autor', max_length=256)
    title = models.CharField('Titel', max_length=256)
    file = models.FileField('Datei hochladen')
    pub_date = models.DateTimeField('Hinzugefügt am', default=datetime.now)

    def __str__(self):
        return self.title
