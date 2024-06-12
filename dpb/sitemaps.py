from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = None
    protocol = "https"

    def items(self):
        return ['dpb', 'bundesordnung', 'pfadfinder', 'impressum', 'datenschutz', 'arbeitskreis', 'kontakt']

    def location(self, item):
        return reverse(item)
