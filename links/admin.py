from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'website')
    search_fields = ['title, website']


admin.site.register(Link, LinkAdmin)
