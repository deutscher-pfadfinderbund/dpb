from django.contrib import admin
from .models import Program

from dpb.admin import PageDownAdmin


class ProgramAdmin(PageDownAdmin):
    list_display = ('title', 'target', 'modified')
    list_filter = ('title', 'created', 'modified')
    search_fields = ['title']
    fieldsets = [
        ('Allgemein', {'fields': ['title', 'target', 'preparation', 'execution', 'greatness']}),
        ('Bilder', {'fields': ['image1', 'image2', 'image3']}),
        ('Ansprechpartner', {'fields': ['contact_name', 'contact_group', 'contact_mail']}),
    ]
    readonly_fields = ('created', 'modified')


admin.site.register(Program, ProgramAdmin)
