# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from django.db import models

from datetime import datetime
from filer.fields.file import FilerFileField
import requests


class State(models.Model):
    """ List of the states of Germany """
    name = models.CharField("Name", max_length=1024, blank=False)
    created = models.DateTimeField("Erstellt am", default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bundesland"
        verbose_name_plural = "Bundesländer"


class Date(models.Model):
    """ Important dates """
    title = models.CharField("Titel", max_length=128, blank=False)
    start = models.DateTimeField("Beginn", blank=True)
    end = models.DateTimeField("Ende", blank=True)
    location = models.CharField("Ort", max_length=128, blank=True)
    latitude = models.FloatField("Breitengrad", max_length=128, blank=True, null=True)
    longitude = models.FloatField("Längengrad", max_length=128, blank=True, null=True)
    display_name = models.CharField("Berechneter Standort", max_length=128, blank=True, null=True)
    description = models.TextField("Beschreibung", blank=True)
    host = models.CharField("Ausrichter", max_length=128, blank=True)
    attachment = FilerFileField(verbose_name="Anhang", null=True, blank=True, related_name="date_attachment")
    created = models.DateTimeField("Erstellt am", default=datetime.now)

    def clean(self):
        try:
            data = requests.get("https://nominatim.openstreetmap.org/search?q=" + str(self.location) + "&format=json&polygon=1&addressdetails=1").json()[0]
            self.latitude = data["lat"]
            self.longitude = data["lon"]
            self.display_name = data["display_name"]
        except:
            self.latitude = None
            self.longitude = None
            self.display_name = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Termine"


class House(models.Model):
    """ Model for Houses and campsites """
    name = models.CharField("* Name des Heimes/Hauses", max_length=4096, blank=False)
    situation = models.CharField("Lage", max_length=4096, blank=True)
    street = models.CharField("Straße", max_length=4096, blank=True)
    plz = models.CharField("PLZ", max_length=4096, blank=True)
    city = models.CharField("Stadt", max_length=4096, blank=True)
    state = models.ForeignKey(State, verbose_name="Bundesland", null=True, blank=True)

    # Web
    gmaps_location = models.URLField("Google Maps Link", blank=True, null=True)
    osm_location = models.URLField("OSM Link", blank=True, null=True)
    latitude = models.FloatField("Breitengrad", max_length=4096, blank=True, null=True)
    longitude = models.FloatField("Längengrad", max_length=4096, blank=True, null=True)
    display_name = models.CharField("Berechneter Standort", max_length=4096, blank=True, null=True)
    website = models.URLField("Link zum Heim/Haus", blank=True, null=True)
    image1 = models.ImageField(upload_to="haeuser", verbose_name="1. Bild", blank=True, null=True)
    image2 = models.ImageField(upload_to="haeuser", verbose_name="2. Bild", blank=True, null=True)
    image3 = models.ImageField(upload_to="haeuser", verbose_name="3. Bild", blank=True, null=True)

    owner = models.CharField("Bundesgruppe des Heimes", max_length=4096, blank=True, null=True)
    contact_name = models.CharField("Ansprechpartner für die Vermietung", max_length=4096, blank=True)
    contact_tel = models.CharField("Telefon", max_length=4096, blank=True, null=True)
    contact_email = models.EmailField("E-Mail", max_length=4096, blank=True, null=True)

    # Schlafmöglichkeiten
    sleep_beds = models.IntegerField("Anzahl der Betten", null=True, blank=True)
    sleep_mattresses = models.IntegerField("Anzahl der Matratzen", null=True, blank=True)
    sleep_floor = models.IntegerField("Fußboden", null=True, blank=True)
    sleep_outdoor = models.TextField("Schlafplätze auf dem Gelände", max_length=4096, blank=True)

    # Ausstattung Küche
    kitchen_stove = models.BooleanField("Herd", default=False, blank=True)
    kitchen_oven = models.BooleanField("Backofen", default=False, blank=True)
    kitchen_fridge = models.BooleanField("Kühlschrank", default=False, blank=True)
    kitchen_sink = models.BooleanField("Spüle", default=False, blank=True)
    kitchen_dishwasher = models.BooleanField("Geschirrspüler", default=False, blank=True)
    kitchen_dishes = models.BooleanField("Geschirr und Besteck", default=False, blank=True)
    kitchen_pots = models.BooleanField("Große Töpfe", default=False, blank=True)
    kitchen_hot_water = models.BooleanField("Heißes Wasser", default=False, blank=True)
    kitchen_other = models.CharField("Sonstige Küchengeräte", max_length=4096, blank=True)

    # Bad
    toilets_separate = models.BooleanField("geschlechtergetrennt", default=False, blank=True)
    toilets_total = models.IntegerField("Anzahl der Toiletten", null=True, blank=True)
    toilets_washbasin = models.IntegerField("Anzahl der Waschbecken", null=True, blank=True)
    toilets_shower = models.IntegerField("Anzahl der Duschen", null=True, blank=True)

    # Gruppenraum
    room_size = models.CharField("Größe", max_length=4096, blank=True)
    room_tables = models.CharField("Anzahl der Tische", max_length=4096, null=True, blank=True)
    room_chairs = models.CharField("Anzahl der Stühle", max_length=4096, null=True, blank=True)

    # Weitere Räume
    rooms_total = models.CharField("Anzahl weiterer Räume", max_length=4096, blank=True)
    rooms_tables = models.CharField("Anzahl der Tische in weiteren Räumen", max_length=4096, blank=True)
    rooms_chairs = models.CharField("Anzahl der Stühle in weiteren Räumen", max_length=4096, blank=True)
    rooms_other = models.TextField("Sonstiges zu den Räumen", max_length=4096, blank=True)

    # Anbindung
    accessibility_parking = models.CharField("Anzahl der Parkplätze", max_length=4096, blank=True)
    accessibility_train = models.CharField("Entfernung zum nächsten Bahnhof", max_length=4096, blank=True)
    accessibility_bus = models.CharField("Entfernung zum nächsten Bus", max_length=4096, blank=True)
    accessibility_shop = models.CharField("Entfernung zur Einkaufsmöglichkeit", max_length=4096, blank=True)
    accessibility_baker = models.CharField("Entfernung zum nächsten Bäcker", max_length=4096, blank=True)
    accessibility_other = models.TextField("Sonstiges in der Nähe", max_length=4096, blank=True)

    # Lage
    location_urban = models.BooleanField("städtisch", default=False, blank=True)
    location_country = models.BooleanField("ländlich", default=False, blank=True)
    location_special = models.TextField("Besonderheiten", max_length=4096, blank=True)

    # Kosten
    price_intern = models.CharField("Preise für Pfadfinder", max_length=4096, blank=True, null=True)
    price_extern = models.CharField("Preise für Externe", max_length=4096, blank=True, null=True)
    price_other = models.TextField("Sonstige Kosten", max_length=4096, blank=True)

    # Sonstiges
    description = models.TextField("Sonstige Beschreibung", blank=True, null=True)

    public = models.BooleanField("Öffentlich?", default=False)
    slug = AutoSlugField(populate_from='name', null=True)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def clean(self):
        try:
            data = requests.get("https://nominatim.openstreetmap.org/search?q=" + str(self.name) + " " + str(self.street) + " " + str(self.plz) + " " + str(self.city) + " " + "&format=json&polygon=1&addressdetails=1").json()[0]
            self.latitude = data["lat"]
            self.longitude = data["lon"]
            self.display_name = data["display_name"]
        except IndexError:
            try:
                data = requests.get("https://nominatim.openstreetmap.org/search?q=" + str(self.street) + " " + str(self.city) + " " + "&format=json&polygon=1&addressdetails=1").json()[0]
                self.latitude = data["lat"]
                self.longitude = data["lon"]
                self.display_name = data["display_name"]
            except IndexError:
                self.latitude = None
                self.longitude = None
                self.display_name = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Haus"
        verbose_name_plural = "Häuser"
