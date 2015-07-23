from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'note')
    list_filter = ['created']
    search_fields = ['name', 'note']

admin.site.register(Feedback, FeedbackAdmin)
