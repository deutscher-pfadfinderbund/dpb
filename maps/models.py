# -*- coding: utf-8 -*-
import requests
from autoslug import AutoSlugField
from django.db import models


def query_latlong(location):
    data = requests.get("https://nominatim.openstreetmap.org/search?q=" + str(location) + " Deutschland" +
                        "&format=json&polygon=1&addressdetails=1").json()[0]
    return data["lat"], data["lon"]


def catch_query(location):
    latitude = longitude = None
    if location:
        try:
            latitude, longitude = query_latlong(location)
        except IndexError:
            latitude = longitude = None
    return latitude, longitude


class GroupMaps(models.Model):
    boysgirls_choices = (
        ("Mädels", "Mädels"),
        ("Jungs", "Jungs"),
        ("Gemischt", "Gemischt"),
    )
    boysgirls = models.CharField("* Mädels / Jungs / gemischt", max_length=256, choices=boysgirls_choices, blank=False)
    group = models.CharField("* Gruppierung (bspw. MS Sturmvögel, JS Hohenstaufen, ...)", max_length=256, blank=False)
    leader = models.CharField("* Unser/e Führer/in ist", max_length=256, blank=False)
    emblem = models.ImageField(verbose_name="Wappen", upload_to="groupmaps", null=True, blank=True)
    subgroups = models.CharField("Untergeordnete Gruppen", max_length=1024, blank=True, null=True)
    special = models.TextField("Das zeichnet uns aus", max_length=4096, blank=True)
    other = models.TextField("Was ihr uns sonst noch mitteilen möchtet", max_length=4096, blank=True)

    location1 = models.CharField("* Standort 1", max_length=1024, blank=False)
    latitude1 = models.FloatField("Breitengrad 1", max_length=4096, blank=True, null=True)
    longitude1 = models.FloatField("Längengrad 1", max_length=4096, blank=True, null=True)
    location2 = models.CharField("Standort 2", max_length=1024, blank=True)
    latitude2 = models.FloatField("Breitengrad 2", max_length=4096, blank=True, null=True)
    longitude2 = models.FloatField("Längengrad 2", max_length=4096, blank=True, null=True)
    location3 = models.CharField("Standort 3", max_length=1024, blank=True)
    latitude3 = models.FloatField("Breitengrad 3", max_length=4096, blank=True, null=True)
    longitude3 = models.FloatField("Längengrad 3", max_length=4096, blank=True, null=True)

    website = models.URLField("Webseite", blank=True)
    slug = AutoSlugField(populate_from='group', unique=True)
    public = models.BooleanField("Öffentlich?", default=False)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def clean(self):
        self.latitude1, self.longitude1 = catch_query(self.location1)
        self.latitude2, self.longitude2 = catch_query(self.location2)
        self.latitude3, self.longitude3 = catch_query(self.location3)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = "Gruppenkarte"
        verbose_name_plural = "Gruppenkarten"
