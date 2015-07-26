from django.contrib import admin

# Register your models here.
from .models import Item


class ItemAdmin(admin.ModelAdmin):
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
