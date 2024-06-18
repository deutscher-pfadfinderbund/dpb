from django.contrib.sitemaps import Sitemap

from .models import Page


class PageSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return Page.objects.filter(registration_required=False).exclude(archived=True)
