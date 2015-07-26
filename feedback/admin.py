from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note', 'archive', 'public')
    list_filter = ['created']
    search_fields = ['name', 'email', 'note', 'archive', 'public']

admin.site.register(Feedback, FeedbackAdmin)
