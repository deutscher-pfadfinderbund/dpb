from django.contrib import admin
from .models import Item
from dpb.admin import PageDownAdmin


class ItemAdmin(PageDownAdmin):
    list_display = ('signature', 'title', 'active', 'reviewed', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['signature', 'title']

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'), 'place',
                                  ('medartdig', 'medartanalog', 'doctype'),
                                  ('file', 'image'), 'keywords', 'location',
                                  'source', 'notes', 'collection', 'amount',
                                  'crossreference', 'owner']}),
        ('Markierungen', {'fields': ['active', 'reviewed', 'pub_date']}),
    ]

admin.site.register(Item, ItemAdmin)
