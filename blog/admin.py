from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'archive', 'public', 'created')
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)