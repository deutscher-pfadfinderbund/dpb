from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Name', max_length=50, blank=False)
    intro = models.TextField('Kurzbeschreibung', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'


class Post(models.Model):
    title = models.CharField('Titel', max_length=50, blank=False)
    author = models.ForeignKey(User, null=True, blank=True, verbose_name="Autor", on_delete=models.SET_NULL)
    content = models.TextField('Inhalt', blank=False)
    slug = AutoSlugField(null=True, populate_from='title')
    archive = models.BooleanField('Archiviert?', default=False)
    file = models.FileField(upload_to='blogpost', verbose_name='Anhang', blank=True, null=True)
    public = models.BooleanField('Öffentlich?', default=True)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)
    category = models.ForeignKey('Category', null=True, verbose_name="Kategorie", on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    class Meta:
        verbose_name = 'Beitrag'
        verbose_name_plural = 'Beiträge'
        ordering = ('-created',)
