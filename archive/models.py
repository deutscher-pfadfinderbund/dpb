from django.db import models

# Create your models here.
class Item(models.Model):
    signature = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    file = models.FileField(default='Keine Datei ausgewählt')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
