from django.db import models
from datetime import datetime

# Create your models here.

class Feedback(models.Model):
    name = models.CharField('Name', max_length=50, default="Anonym", blank=True)
    note = models.TextField('Anmerkung', max_length=1024, blank=False)
    created = models.DateTimeField('Erstellt am', default=datetime.now)
