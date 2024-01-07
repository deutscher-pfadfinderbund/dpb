import re

from django.contrib import admin
from django.db.models import QuerySet, Value
from django.db.models.functions import Coalesce, Substr, NullIf, StrIndex, Length
from django.http import HttpRequest

from dpb.admin import PageDownAdmin
from .models import Feedback, Item, Year, DocType


class AlphanumericSignatureFilter(admin.SimpleListFilter):
    title = 'Signatur (alphanumerisch)'
    parameter_name = 'signature_alphanumeric'

    def lookups(self, request, model_admin):
        return (
            ('signature', 'Signatur (alphanumerisch)'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'signature':
            return queryset.order_by(
                Coalesce(Substr('signature', Value(0), NullIf(StrIndex('signature', Value(' ')), Value(0))),
                         'signature'),
                Length('signature'),
                'signature'
            )


class HasFileFilter(admin.SimpleListFilter):
    title = 'Digital?'
    parameter_name = 'has_file'

    def lookups(self, request: HttpRequest, model_admin):
        """
        Possible selections in the admin-filter section

        :param request:
        :param model_admin:
        :return:
        """
        return (
            ('digital', 'digital'),
            ('nicht digital', 'nicht digital'),
        )

    def queryset(self, request: HttpRequest, queryset: QuerySet):
        """
        Filter items by presence of file. self.value() is the selection in the django admin and possible values are
        from lookups/3.

        :param request:
        :param queryset:
        :return:
        """
        if self.value() == 'digital':
            return queryset.exclude(file__isnull=True)
        if self.value() == 'nicht digital':
            return queryset.exclude(file__isnull=False)
        return queryset


def human_key(key):
    """
    Sort collection as humans would do it.

    :param key:
    :return:
    """
    parts = re.split(r'(\d*\.\d+|\d+)', key)
    return tuple((e.swapcase() if i % 2 == 0 else float(e))
                 for i, e in enumerate(parts))


class ItemAdmin(PageDownAdmin):
    list_display = (
        'title', 'author', 'year', 'medartanalog', 'signature', 'location', 'has_file', 'reviewed',
    )
    list_filter = [AlphanumericSignatureFilter, 'medartanalog', 'doctype', 'reviewed', HasFileFilter]
    search_fields = ['signature', 'title', 'author', 'keywords', 'notes']

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year'),
                                  'place',
                                  ('medartanalog', 'document_type'),
                                  'file', 'file2', 'file3',
                                  'keywords', 'location',
                                  'source', 'notes', 'collection', 'amount',
                                  'crossreference', 'owner']}),
        ('Markierungen', {'fields': ['active', 'reviewed', 'pub_date']}),
    ]
    save_as = True
    readonly_fields = ['pub_date']


class YearAdmin(PageDownAdmin):
    list_display = ('year',)
    fieldsets = [
        ('Allgemein', {'fields': ['year']}),
    ]
    readonly_fields = ('created',)


class FeedbackAdmin(PageDownAdmin):
    list_display = ('name', 'email', 'archive', 'mailto_link')
    list_filter = ['created']
    search_fields = ['name', 'email', 'note', 'archive']
    actions = ['to_archive']
    readonly_fields = ('created', 'modified', 'mailto_link')
    fieldsets = [
        ('Allgemein', {'fields': [
            'name', ('email', 'mailto_link'), 'group',
            'note', 'item'
        ]}),
        ('Meta', {'fields': [
            'archive', 'created', 'modified'
        ]})
    ]

    def to_archive(self, request, queryset):
        queryset.update(archive=True)

    to_archive.short_description = "Markierte Einträge als bearbeitet markieren"

class ItemInline(admin.TabularInline):
    model = Item
    fields = ['title']
    readonly_fields = ['signature']
    show_change_link = True
    extra = 0  # Number of empty forms to display

class DocumentTypeAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(DocType, DocumentTypeAdmin)
