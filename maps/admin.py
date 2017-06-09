from django.contrib import admin
from .models import GroupMaps


@admin.register(GroupMaps)
class GroupMapsAdmin(admin.ModelAdmin):
    list_display = ("group", "location1")
    search_fields = ["group"]
    readonly_fields = ["latitude1", "longitude1", "latitude2", "longitude2", "latitude3", "longitude3"]
    fieldsets = [
        ("Allgemein", {"fields": ["boysgirls", "group", "leader", "emblem", "subgroups", "special", "other", "website",
                                  "public"]}),
        ("Locations", {"fields": [
            ("location1", "latitude1", "longitude1"),
            ("location2", "latitude2", "longitude2"),
            ("location3", "latitude3", "longitude3"),
        ]}),
    ]
