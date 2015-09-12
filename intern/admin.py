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


admin.site.register(Date, DateAdmin)