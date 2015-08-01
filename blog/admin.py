from django.contrib import admin

from .models import Post, Category
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'category', 'archive', 'public', 'created')
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)