from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }