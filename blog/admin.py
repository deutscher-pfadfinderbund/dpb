from django.contrib import admin

from .models import Post, Category
from dpb.admin import PageDownAdmin


class PostAdmin(PageDownAdmin):
    list_display = ('title', 'category', 'archive', 'public', 'created')
    list_filter = ['created']
    search_fields = ['title']
    fieldsets = [
        (None,        {'fields': ['title', 'category', ('archive', 'public'), 'content']}),
        ('Erweitert', {'fields': ['created', 'author'], 'classes': ['collapse']}),
    ]

    def save_model(self, request, obj, form, change):
        # Automatic set author if None is set
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Category)