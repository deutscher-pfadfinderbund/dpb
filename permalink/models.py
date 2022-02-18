from django.db import models


class Permalink(models.Model):
    label = models.CharField('Bezeichner', max_length=128, blank=True)
    short = models.SlugField('Von', blank=False, unique=True)
    redirect_url = models.URLField('Redirect', blank=False)

    def __str__(self):
        return f"{self.label} {self.short} -> {self.redirect_url}"
