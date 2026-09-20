# -*- coding: utf-8 -*-

import logging
import requests
from autoslug import AutoSlugField
from django.db import models

logger = logging.getLogger(__name__)

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
NOMINATIM_TIMEOUT = 10  # seconds
# Nominatim rejects requests that do not identify their client.
NOMINATIM_USER_AGENT = "dpb-website (website@deutscher-pfadfinderbund.de)"

class State(models.Model):
    """ List of the states of Germany """
    name = models.CharField("Name", max_length=1024, blank=False)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bundesland"
        verbose_name_plural = "Bundesländer"


class House(models.Model):
    """ Model for Houses and campsites """
    name = models.CharField("* Name des Heimes/Hauses", max_length=4096, blank=False)
    situation = models.CharField("Lage", max_length=4096, blank=True)
    street = models.CharField("Straße", max_length=4096, blank=True)
    plz = models.CharField("PLZ", max_length=4096, blank=True)
    city = models.CharField("Stadt", max_length=4096, blank=True)
    state = models.ForeignKey(State, verbose_name="Bundesland", null=True, blank=True, on_delete=models.SET_NULL)

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

    user = models.CharField("Dein Name", max_length=1024, blank=True)
    user_mail = models.EmailField("Deine E-Mail Adresse", max_length=1024, blank=True)

    public = models.BooleanField("Öffentlich?", default=False)
    slug = AutoSlugField(populate_from='name', null=True)
    created = models.DateTimeField("Erstellt am", auto_now_add=True)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def address_fields(self):
        """The fields the geocoding result depends on."""
        return (self.name, self.street, self.plz, self.city, self.state_id)

    def geocode(self):
        """
        Look the address up with Nominatim and return (lat, lon, display_name),
        or None when it cannot be resolved.

        Nominatim's usage policy requires every client to identify itself; a
        request sent with the requests library's default user agent is answered
        with 403, so the header below is not optional.
        https://operations.osmfoundation.org/policies/nominatim/
        """
        headers = {"User-Agent": NOMINATIM_USER_AGENT}
        default_params = {
            "format": "json",
            "polygon": 1,
            "addressdetails": 1,
            "accept-language": "de",
        }
        query_params = {
            "amenity": self.name,
            "street": self.street,
            "postalcode": self.plz,
            "city": self.city,
            "state": str(self.state) if self.state else None,
        }

        try:
            for params in (query_params, {**query_params, "amenity": None}):
                response = requests.get(
                    NOMINATIM_URL,
                    params=default_params | params,
                    headers=headers,
                    timeout=NOMINATIM_TIMEOUT,
                )
                if response.status_code != 200:
                    logger.warning(
                        "Nominatim answered %s for %r", response.status_code, self.name
                    )
                    return None
                results = response.json()
                if results:
                    data = results[0]
                    return data["lat"], data["lon"], data["display_name"]
        except requests.exceptions.RequestException as e:
            logger.warning("Error querying OpenStreetMap for %r", self.name, exc_info=e)
            return None

        logger.info("Nominatim found no match for %r", self.name)
        return None

    def clean(self):
        # Only ask Nominatim when the address actually changed, or when we have
        # no coordinates yet. Geocoding on every save would both hammer a
        # rate-limited service and, on any hiccup, drop coordinates that were
        # already correct just because somebody fixed a typo elsewhere.
        previous = House.objects.filter(pk=self.pk).first() if self.pk else None
        unchanged = previous is not None and previous.address_fields() == self.address_fields()
        if unchanged and self.latitude is not None and self.longitude is not None:
            return

        location = self.geocode()
        if location is None:
            # Keep whatever we had rather than blanking a working map.
            return

        self.latitude, self.longitude, self.display_name = location

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Haus"
        verbose_name_plural = "Häuser"
