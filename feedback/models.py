# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

# Create your models here.

class Feedback(models.Model):
    name = models.CharField('Name', max_length=50, default="Anonym", blank=True)
    email = models.EmailField('E-Mail', max_length=254, blank=True)
    note = models.TextField('Anmerkung', max_length=1024, blank=False)
    answer = models.TextField('Antwort', max_length=1024, blank=True)
    author = models.CharField('Antwort von', max_length=50, default="Admin", blank=True)
    archive = models.BooleanField('Bearbeitet?', default=False)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField('Erstellt am', default=datetime.now)
