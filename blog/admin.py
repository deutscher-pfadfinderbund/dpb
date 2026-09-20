from django.contrib import admin

from dpb.admin import PageDownAdmin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(PageDownAdmin):
    list_display = ('title', 'category', 'archive', 'public', 'created')
    list_filter = ['created']
    search_fields = ['title']
    readonly_fields = ['created']
    fieldsets = [
        (None, {'fields': ['title', 'category', 'file', ('archive', 'public'), 'content']}),
        ('Erweitert', {'fields': ['created', 'author'], 'classes': ['collapse']}),
    ]

    def get_queryset(self, request):
        """Optimize queryset with select_related for foreign keys"""
        queryset = super().get_queryset(request)
        return queryset.select_related('category', 'author')

    def save_model(self, request, obj, form, change):
        # Automatic set author if None is set
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Category)
