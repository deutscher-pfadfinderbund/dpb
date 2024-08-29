from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http.response import HttpResponsePermanentRedirect
from django.urls import path, re_path, include

from blog import views as blogviews
from pages import views as pageviews
from pages.sitemaps import PageSitemap
from . import views
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'pages': PageSitemap
}

urlpatterns = [re_path(r'^$', views.index, name='index'),
               re_path(r'^bundesordnung/$', views.BundesordnungView.as_view(), name='bundesordnung'),
               re_path(r'^dpb/$', views.DPBView.as_view(), name='dpb'),
               re_path(r'^pfadfinder/$', views.PfadfinderView.as_view(), name='pfadfinder'),

               # Apps
               re_path(r'^bundesarchiv/', include('archive.urls')),
               re_path(r'^kontakt/', include('contact.urls')),
               re_path(r'^links/', include('links.urls')),
               re_path(r'^filer/', include('filer.urls')),
               re_path(r'^([sx]|[lL](?:ink)?)/', include('permalink.urls')), 
               re_path(r'^vorfreude/', include('vorfreude.urls')),

               # Members Area
               re_path(r'^intern/', include('intern.urls')),
               re_path(r'^infos/$', blogviews.blog_overview, {'category': 'Aktuelles'}, name='blog_page'),
               re_path(r'^infos/seite/(?P<page>[0-9]+)/$', blogviews.blog_overview, {'category': 'Aktuelles'},
                       name='blog_page'),
               re_path(r'^infos/(?P<slug>[\w-]+)/$', blogviews.post, name='blog_detail'),
               re_path(r'^infos/neu/$', blogviews.PostCreate.as_view(), name='blog_post_add'),
               re_path(r'^infos/bearbeiten/(?P<pk>[0-9]+)/$', blogviews.PostUpdate.as_view(), name='blog_post_change'),
               re_path(r'^infos/entfernen/(?P<pk>[0-9]+)/$', blogviews.PostDelete.as_view(), name='blog_post_delete'),
               re_path(r'^intern/themen/$', blogviews.blog_overview, {'category': 'Themen'}, name='blog_themen'),
               re_path(r'^intern/arbeitskreis/mitglieder/$', pageviews.page,
                       {'url': '/intern/arbeitskreis/mitglieder/'},
                       name='arbeitskreis_mitglieder'),
               re_path(r'^intern/bundesgilde/$', pageviews.page, {'url': '/intern/bundesgilde/'}, name='bundesgilde'),

               re_path(r'^heimabende/', include('evening_program.urls')),
               re_path(r'^karten/',
                       view=lambda _: HttpResponsePermanentRedirect('https://karte.deutscher-pfadfinderbund.de')),

               re_path(r'^admin/', admin.site.urls),
               re_path(r'^', include('django.contrib.auth.urls')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    re_path(r'^impressum/$', pageviews.page, {'url': '/impressum/'}, name='impressum'),
    re_path(r'^datenschutz/$', pageviews.page, {'url': '/datenschutz/'}, name='datenschutz'),
    re_path(r'^arbeitskreis/$', pageviews.page, {'url': '/arbeitskreis/'}, name='arbeitskreis'),

    re_path(r'^kontakt/$', pageviews.page, {'url': '/kontakt/'}, name='kontakt'),

    re_path(r'^(?P<url>.*/)$', pageviews.page, name='page'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
