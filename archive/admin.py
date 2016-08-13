from django.contrib import admin
from .models import Item
from dpb.admin import PageDownAdmin


class ItemAdmin(PageDownAdmin):
    list_display = ('title', 'author', 'doctype', 'active', 'reviewed', 'signature')
    list_filter = ['doctype']
    search_fields = ['signature', 'title', 'author']

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'),
                                  'years',
                                  'place',
                                  ('medartdig', 'medartanalog', 'doctype'),
                                  ('file', 'image'), 'keywords', 'location',
                                  'source', 'notes', 'collection', 'amount',
                                  'crossreference', 'owner']}),
        ('Markierungen', {'fields': ['active', 'reviewed', 'pub_date']}),
    ]
    readonly_fields = ['pub_date']

admin.site.register(Item, ItemAdmin)
