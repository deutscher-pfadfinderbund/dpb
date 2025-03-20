from django.contrib import admin

from .models import Permalink

@admin.register(Permalink)
class PermalinkAdmin(admin.ModelAdmin):
  list_display = ["label", "short", "redirect_url"]
