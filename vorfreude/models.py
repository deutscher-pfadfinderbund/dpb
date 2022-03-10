from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    fahrtenname = models.CharField("Name von Dir oder Deiner Gruppe", max_length=128, blank=False)
    foto = models.ImageField("Foto")
    bundesgruppe = models.CharField("Bundesgliederung", max_length=256)
    gedanken = models.TextField("Wenn ich (wir) an das Bundeslager 2022 denke(n), dann...", blank=False)
    sagen = models.TextField("Und was ich (wir) noch gerne sagen möchte(n)...", blank=False)
    created = models.DateTimeField("Erstellt am", default=timezone.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Beitrag von {self.fahrtenname}"
