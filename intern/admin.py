from django.contrib import admin

from .models import Date


class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start', 'end')
    list_filter = ['start']
    search_fields = ['title']
    fieldsets = [
        (None,        {'fields': ['title', 'start', 'end', 'attachment', 'location', 'location_gmaps', 'description', 'host']}),
        ('Erweitert', {'fields': ['created'], 'classes': ['collapse']}),
    ]


admin.site.register(Date, DateAdmin)