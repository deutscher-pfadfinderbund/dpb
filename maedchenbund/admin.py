from django.contrib import admin

from dpb.admin import PageDownAdmin
from .models import Document


class DocumentAdmin(PageDownAdmin):
    list_display = ('title', 'created', 'modified')
    list_filter = ('title', 'created', 'modified')
    search_fields = ['title']


admin.site.register(Document, DocumentAdmin)
