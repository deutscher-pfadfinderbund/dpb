from django.contrib import admin

from dpb.admin import PageDownAdmin
from .models import Feedback


class FeedbackAdmin(PageDownAdmin):
    list_display = ('name', 'email', 'note', 'archive', 'public')
    list_filter = ['created']
    search_fields = ['name', 'email', 'note', 'archive', 'public']

    actions = ['to_archive']

    def to_archive(self, _request, queryset):
        queryset.update(archive=True)

    to_archive.short_description = "Markierte Einträge archivieren"


admin.site.register(Feedback, FeedbackAdmin)
