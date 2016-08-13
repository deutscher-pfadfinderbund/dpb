from django.contrib import admin
from .models import Item, Year
from dpb.admin import PageDownAdmin


class ItemAdmin(PageDownAdmin):
    list_display = ('title', 'author', 'doctype', 'active', 'reviewed', 'signature')
    list_filter = ['doctype']
    search_fields = ['signature', 'title', 'author']
    filter_horizontal = ('years',)

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'),
                                  'years',
                                  'place',
                                  ('doctype', 'medartdig', 'medartanalog'),
                                  ('file', 'image'), 'keywords', 'location',
                                  'source', 'notes', 'collection', 'amount',
                                  'crossreference', 'owner']}),
        ('Markierungen', {'fields': ['active', 'reviewed', 'pub_date']}),
    ]
    readonly_fields = ['pub_date']


class YearAdmin(PageDownAdmin):
    list_display = ('year',)
    fieldsets = [
        ('Allgemein', {'fields': ['year']}),
    ]
    readonly_fields = ('created',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Year, YearAdmin)
