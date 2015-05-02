from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('signature', 'title', 'public','pub_date')
    list_filter = ['pub_date']
    search_fields = ['signature', 'title']

admin.site.register(Item, ItemAdmin)
