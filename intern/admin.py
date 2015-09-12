from django.contrib import admin

from .models import Date


class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start', 'end')
    list_filter = ['start']
    search_fields = ['title']
    readonly_fields = ['latitude', 'longitude', 'display_name']
    fieldsets = [
        (None,        {'fields': ['title', 'start', 'end', 'attachment', 'location', 'host', 'description']}),
        ('Erweitert', {'fields': ['created', 'latitude', 'longitude', 'display_name'], 'classes': ['collapse']}),
    ]

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'price_intern')
    list_filter = ['name', 'price_intern']
    search_fields = ['name', 'city']
    readonly_fields = ['latitude', 'longitude', 'display_name']
    fieldsets = [
        (None,        {'fields': ['name',
                                  ('street', 'plz', 'city'),
                                  ('gmaps_location', 'osm_location'),
                                  'website', 'image', 'owner',
                                  ('contact_name', 'contact_tel', 'contact_email'),
                                  'description',
                                  ('capacity_house', 'capacity_outdoor'),
                                  ('price_intern', 'price_extern')]}),
        ('Erweitert', {'fields': ['created', 'latitude', 'longitude', 'display_name'], 'classes': ['collapse']}),
    ]


admin.site.register(Date, DateAdmin)