from django.contrib import admin

from dpb.admin import PageDownAdmin
from .models import Feedback, Item, Year


class ItemAdmin(PageDownAdmin):
    list_display = ('title', 'author', 'year', 'medartanalog', 'signature', 'location',)
    list_filter = ['medartanalog', 'year']
    search_fields = ['signature', 'title', 'author']
    filter_horizontal = ('years',)

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'),
                                  'place',
                                  ('medartanalog', 'doctype'),
                                  'file',
                                  'keywords', 'location',
                                  'source', 'notes', 'collection', 'amount',
                                  'crossreference', 'owner']}),
        ('Markierungen', {'fields': ['active', 'reviewed', 'pub_date']}),
    ]
    save_as = True
    readonly_fields = ['pub_date']
    ordering = ('-modified',)


class YearAdmin(PageDownAdmin):
    list_display = ('year',)
    fieldsets = [
        ('Allgemein', {'fields': ['year']}),
    ]
    readonly_fields = ('created',)


class FeedbackAdmin(PageDownAdmin):
    list_display = ('name', 'email', 'note', 'archive')
    list_filter = ['created']
    search_fields = ['name', 'email', 'note', 'archive']
    actions = ['to_archive']
    readonly_fields = ('created', 'modified')

    def to_archive(self, request, queryset):
        queryset.update(archive=True)
    to_archive.short_description = "Markierte Einträge als bearbeitet markieren"


admin.site.register(Item, ItemAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Feedback, FeedbackAdmin)
