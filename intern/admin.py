from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models
from .models import Date, House, State


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start', 'end')
    list_filter = ['start']
    search_fields = ['title']
    readonly_fields = ['latitude', 'longitude', 'display_name']
    fieldsets = [
        (None,        {'fields': ['title', 'start', 'end', 'attachment', 'location', 'host', 'description']}),
        ('Erweitert', {'fields': ['created', 'latitude', 'longitude', 'display_name'], 'classes': ['collapse']}),
    ]


@admin.register(House)
class HouseAdmin(PageDownAdmin):
    list_display = ('name', 'city', 'price_intern')
    list_filter = ['name', 'price_intern']
    search_fields = ['name', 'city']
    readonly_fields = ['latitude', 'longitude', 'display_name']
    fieldsets = [
        ('Allgemein', {'fields': [
            'name',
            ('street', 'plz', 'city'),
            ('situation', 'state'),
            'accessibility',
            'website',
            ('image1', 'image2', 'image3'),
            'description',
            ('gmaps_location', 'osm_location')]}),
            ('Kontakt', {'fields': [
            'owner',
            ('contact_name', 'contact_tel', 'contact_email')]}),
            ('Preise', {'fields': [
            ('capacity_house', 'capacity_outdoor'),
            ('price_intern', 'price_extern')]}),
        ('Erweitert', {'fields': ['created', 'latitude', 'longitude', 'display_name'], 'classes': ['collapse']}),
    ]

admin.site.register(State)