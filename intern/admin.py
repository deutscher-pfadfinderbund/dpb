from django.contrib import admin

from .models import Date


class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'location', 'created')
    list_filter = ['start']
    search_fields = ['title']
    fieldsets = [
        (None,        {'fields': ['title', 'start', 'end', 'location', 'location_gmaps', 'description', 'host']}),
        ('Erweitert', {'fields': ['created'], 'classes': ['collapse']}),
    ]


admin.site.register(Date, DateAdmin)