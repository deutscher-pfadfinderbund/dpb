from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, reverse

from blog import views as blogviews
from pages import views as pageviews
from pages.sitemaps import PageSitemap
from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^bundesordnung/$', views.BundesordnungView.as_view(), name='bundesordnung'),
               url(r'^dpb/$', views.DPBView.as_view(), name='dpb'),
               url(r'^pfadfinder/$', views.PfadfinderView.as_view(), name='pfadfinder'),

               # Apps
               url(r'^bundesarchiv/', include('archive.urls')),
               url(r'^kontakt/', include('contact.urls')),
               url(r'^links/', include('links.urls')),
               url(r'^filer/', include('filer.urls')),
               url(r'^l/', include('permalink.urls')),
               url(r'^vorfreude/', include('vorfreude.urls')),

               # Members Area
               url(r'^intern/', include('intern.urls')),
               url(r'^infos/$', blogviews.blog_overview, {'category': 'Aktuelles'}, name='blog_page'),
               url(r'^infos/seite/(?P<page>[0-9]+)/$', blogviews.blog_overview, {'category': 'Aktuelles'},
                   name='blog_page'),
               url(r'^infos/(?P<slug>[\w-]+)/$', blogviews.post, name='blog_detail'),
               url(r'^infos/neu/$', blogviews.PostCreate.as_view(), name='blog_post_add'),
               url(r'^infos/bearbeiten/(?P<pk>[0-9]+)/$', blogviews.PostUpdate.as_view(), name='blog_post_change'),
               url(r'^infos/entfernen/(?P<pk>[0-9]+)/$', blogviews.PostDelete.as_view(), name='blog_post_delete'),
               url(r'^intern/themen/$', blogviews.blog_overview, {'category': 'Themen'}, name='blog_themen'),
               url(r'^intern/arbeitskreis/mitglieder/$', pageviews.page, {'url': '/intern/arbeitskreis/mitglieder/'},
                   name='arbeitskreis_mitglieder'),
               url(r'^intern/bundesgilde/$', pageviews.page, {'url': '/intern/bundesgilde/'}, name='bundesgilde'),

               url(r'^heimabende/', include('evening_program.urls')),
               url(r'^karten/', include('maps.urls')),

               url(r'^admin/', admin.site.urls),
               url(r'^tinymce/', include('tinymce.urls')),
               url(r'^', include('django.contrib.auth.urls')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^impressum/$', pageviews.page, {'url': '/impressum/'}, name='impressum'),
    url(r'^datenschutz/$', pageviews.page, {'url': '/datenschutz/'}, name='datenschutz'),
    url(r'^arbeitskreis/$', pageviews.page, {'url': '/arbeitskreis/'}, name='arbeitskreis'),

    url(r'^kontakt/$', pageviews.page, {'url': '/kontakt/'}, name='kontakt'),

    url(r'^(?P<url>.*/)$', pageviews.page, name='page'),
]


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = None

    def items(self):
        return ['dpb', 'bundesordnung', 'pfadfinder', 'impressum', 'datenschutz', 'arbeitskreis', 'kontakt']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'static': StaticViewSitemap,
    'pages': PageSitemap
}

urlpatterns.append(path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'))
