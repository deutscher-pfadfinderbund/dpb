from django.db import models

# Create your models here.
class Item(models.Model):
    signature = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
