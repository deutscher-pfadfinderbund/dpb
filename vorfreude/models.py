from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    fahrtenname = models.CharField("(Fahrten-)Name", max_length=128, blank=False)
    foto = models.ImageField("Foto")
    gilde = models.CharField("Name der Gilde / Horte", max_length=128)
    bundesgruppe = models.CharField("Bundesgruppe", max_length=256)
    gedanken = models.TextField("Wenn ich an den Bund denke, dann...", blank=False)
    sagen = models.TextField("Und was ich / wir noch sagen möchte...", blank=False)
    created = models.DateTimeField("Erstellt am", default=timezone.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
