from django.contrib import admin
from .models import Item, Year
from dpb.admin import PageDownAdmin


class ItemAdmin(PageDownAdmin):
    list_display = ('title', 'author', 'medartanalog', 'active', 'reviewed', 'signature', 'modified')
    list_filter = ['medartanalog']
    search_fields = ['signature', 'title', 'author']
    filter_horizontal = ('years',)

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'),
                                  'years',
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


admin.site.register(Item, ItemAdmin)
admin.site.register(Year, YearAdmin)
