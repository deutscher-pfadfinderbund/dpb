from django.contrib import admin
from django.db.models import QuerySet, Value
from django.db.models.fields import TextField
from django.db.models.functions import Concat, LPad, Cast
from django.http import HttpRequest

from dpb.admin import PageDownAdmin
from .models import Feedback, Item, Year, DocType


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

class YearFilter(admin.SimpleListFilter):
    title = 'Jahr'
    parameter_name = 'year'

    def lookups(self, request: HttpRequest, model_admin):
        years = Item.objects.values_list('year', flat=True).distinct().order_by('year').reverse()
        return [(str(year), str(year)) for year in years if year is not None]

    def queryset(self, request: HttpRequest, queryset: QuerySet):
        if self.value():
            year = int(self.value())
            return queryset.filter(year=year)
        return queryset

class ItemAdmin(PageDownAdmin):
    list_display = (
        'title', 'author', 'yyyymmdd', 'medartanalog', 'signature', 'location', 'has_file', 'reviewed',
    )
    list_filter = ['medartanalog', 'document_type', 'reviewed', HasFileFilter, YearFilter]
    search_fields = ['signature', 'title', 'author', 'keywords', 'notes']

    fieldsets = [
        ('Allgemein', {'fields': ['signature', 'title', 'author',
                                  ('date', 'year', 'month', 'day'),
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

    def get_queryset(self, request):
        """Optimize queryset with select_related for foreign keys"""
        queryset = super().get_queryset(request)
        return queryset.select_related('document_type')

    @admin.display(description='Datum', ordering=Concat('year', LPad(Cast('month', TextField()), 2, Value("0")), LPad(Cast('day', TextField()), 2, Value("0"))))
    def yyyymmdd(self, item: Item) -> str:
        """Return yyyy, yyyy-mm or yyyy-mm-dd depending on available data"""

        if item.year is not None and item.month and item.day:
            return f"{item.year:d}-{item.month:02d}-{item.day:02d}"
        elif item.year is not None and item.month:
            return f"{item.year:d}-{item.month:02d}"
        elif item.year is not None:
            return f"{item.year:d}"
        else:
            return ""


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

    def get_queryset(self, request):
        """Optimize queryset with select_related for foreign keys"""
        queryset = super().get_queryset(request)
        return queryset.select_related('item')

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
