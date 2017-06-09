from django.apps import apps as django_apps
from django.contrib.sitemaps import Sitemap
from django.core.exceptions import ImproperlyConfigured


class PageSitemap(Sitemap):
    def items(self):
        if not django_apps.is_installed('django.contrib.sites'):
            raise ImproperlyConfigured("PageSitemap requires django.contrib.sites, which isn't installed.")
        site = django_apps.get_model('sites.Site')
        current_site = site.objects.get_current()
        return current_site.page_set.filter(registration_required=False)
