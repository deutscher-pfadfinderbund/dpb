from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note', 'archive', 'public')
    list_filter = ['created']
    search_fields = ['name', 'email', 'note', 'archive', 'public']

    actions = ['to_archive']

    def to_archive(self, request, queryset):
        queryset.update(archive=True)
    to_archive.short_description = "Markierte Einträge archivieren"

admin.site.register(Feedback, FeedbackAdmin)
