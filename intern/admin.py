from django.contrib import admin

from .models import Date


class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'created')
    list_filter = ['date']
    search_fields = ['title']
    fieldsets = [
        (None,        {'fields': ['title', 'date', 'location', 'location_gmaps', 'description', 'host']}),
        ('Erweitert', {'fields': ['created'], 'classes': ['collapse']}),
    ]


admin.site.register(Date, DateAdmin)