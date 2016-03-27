from django.contrib import admin
from .models import Document, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    readonly_fields = ["created", "modified"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        ("Allgemein", {"fields": ["name", "category", "file", "description"]}),
        ("Erweitert", {"fields": ["created", "modified"], "classes": ["collapse"]}),
    ]
