from django.contrib import admin
from .models import Link, LinkCategory


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'website')
    search_fields = ['title']


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory)