from django.db import models

class Item(models.Model):
    signature = models.CharField('Signatur', max_length=256)
    author = models.CharField('Autor', max_length=256)
    title = models.CharField('Titel', max_length=256)
    file = models.FileField('Pfad lokale Datei', default='Keine Datei ausgewählt')
    pub_date = models.DateTimeField('Hinzugefügt am')

    def __str__(self):
        return self.title
