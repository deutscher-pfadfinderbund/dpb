from django.contrib import admin
from .models import Date, House, State
from dpb.admin import PageDownAdmin


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start", "end")
    list_filter = ["start"]
    search_fields = ["title"]
    readonly_fields = ["latitude", "longitude", "display_name"]
    fieldsets = [
        (None,        {"fields": ["title", "start", "end", "attachment", "location", "host", "description"]}),
        ("Erweitert", {"fields": ["created", "latitude", "longitude", "display_name"], "classes": ["collapse"]}),
    ]


@admin.register(House)
class HouseAdmin(PageDownAdmin):
    list_display = ("name", "state", "city", "price_intern", "public")
    list_filter = ["name", "price_intern"]
    search_fields = ["name", "city"]
    readonly_fields = ["latitude", "longitude", "display_name", "modified"]
    fieldsets = [
        ("Allgemein", {"fields": [
            "name",
            "public",
            "situation",
            ("street", "plz", "city"),
            "state"
        ]}),
        ("Schlafmöglichkeiten", {"fields": [
            ("sleep_beds", "sleep_mattresses", "sleep_floor"),
            "sleep_outdoor",
        ]}),
        ("Ausstattung Küche", {"fields": [
            ("kitchen_stove", "kitchen_oven", "kitchen_fridge"),
            ("kitchen_sink", "kitchen_dishwasher", "kitchen_dishes"),
            ("kitchen_pots", "kitchen_hot_water"),
            "kitchen_other",
        ]}),
        ("Bad", {"fields": [
            "toilets_separate",
            ("toilets_total", "toilets_washbasin", "toilets_shower"),
        ]}),
        ("Gruppenraum", {"fields": [
            ("room_size", "room_tables", "room_chairs"),
        ]}),
        ("Weitere Räume", {"fields": [
            ("rooms_total", "rooms_tables", "rooms_chairs"),
            "rooms_other"
        ]}),
        ("Anbindung", {"fields": [
            ("accessibility_parking", "accessibility_train", "accessibility_bus"),
            ("accessibility_shop", "accessibility_baker"),
            "accessibility_other",
        ]}),
        ("Lage", {"fields": [
            ("location_urban", "location_country"),
            "location_special",
        ]}),
        ("Web", {"fields": [
            "website",
            ("image1", "image2", "image3"),
            ("gmaps_location", "osm_location")
        ]}),
        ("Kontakt", {"fields": [
            "owner",
            ("contact_name", "contact_tel", "contact_email")
        ]}),
        ("Kosten", {"fields": [
            ("price_intern", "price_extern"),
            "price_other",
        ]}),
        ("Sonstiges", {"fields": [
            "description",
        ]}),
        ("Erweitert", {"fields": [
            ("latitude", "longitude"),
            "display_name",
            "created",
            "modified",
        ], "classes": ["collapse"]}),
    ]

admin.site.register(State)