from django.contrib import admin
from .models import Link, LinkCategory

from dpb.admin import PageDownAdmin


class LinkAdmin(PageDownAdmin):
    list_display = ('title', 'category', 'website')
    list_filter = ('category',)
    search_fields = ['title']


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory)
