from django.contrib import admin
from .models import Link, LinkCategory

from dpb.admin import PageDownAdmin


class LinkAdmin(PageDownAdmin):
    list_display = ('title', 'state', 'category', 'website')
    list_filter = ('category',)
    search_fields = ['title']

    def get_queryset(self, request):
        """Optimize queryset with select_related for foreign keys"""
        queryset = super().get_queryset(request)
        return queryset.select_related('state', 'category')


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory)
