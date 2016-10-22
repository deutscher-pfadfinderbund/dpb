# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from django.db import models
from datetime import datetime


class Program(models.Model):
    title = models.CharField("Titel", max_length=256, blank=False)
    target = models.CharField("Wie alt sind meine Mädchen / Jungen?", max_length=128, blank=False)
    preparation = models.TextField("Was habe ich vorbereitet?", max_length=4096, blank=True)
    execution = models.TextField("Was haben wir gemacht?", max_length=4096, blank=False)
    greatness = models.TextField("Was war daran so toll?", max_length=4096, blank=True)
    contact_name = models.CharField("Mein Name", max_length=128, blank=True)
    contact_group = models.CharField("Meine Gruppe", max_length=128, blank=True)
    contact_mail = models.EmailField("Meine E-Mail", blank=True)
    file1 = models.FileField(upload_to="heimabende", verbose_name="1. Anhang", blank=True, null=True)
    file2 = models.FileField(upload_to="heimabende", verbose_name="2. Anhang", blank=True, null=True)
    file3 = models.FileField(upload_to="heimabende", verbose_name="3. Anhang", blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateTimeField("Erstellt am", default=datetime.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def __str__(self):
        return str(self.title)

    @staticmethod
    def get_absolute_url():
        from django.core.urlresolvers import reverse
        return reverse('evening_program:index')

    class Meta:
        verbose_name = 'Heimabendprogramm'
        verbose_name_plural = 'Heimabendprogramme'
        ordering = ('created',)
