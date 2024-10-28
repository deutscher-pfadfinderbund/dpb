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

urlpatterns = [path("", views.index, name='index'),
               path("bundesordnung/", views.BundesordnungView.as_view(), name="bundesordnung"),
               path("dpb/", views.DPBView.as_view(), name="dpb"),
               path("pfadfinder/", views.PfadfinderView.as_view(), name="pfadfinder"),

               # Apps
               path("bundesarchiv/", include('archive.urls')),
               path('kontakt/', include('contact.urls')),
               path('links/', include('links.urls')),
               path('filer/', include('filer.urls')),
               path('l/', include('permalink.urls')),
               re_path(r'^(?:[sx]|[lL](?:ink)?)/', include('permalink.urls')),
               path('vorfreude/', include('vorfreude.urls')),

               # Members Area
               path('intern/', include('intern.urls')),
               path('infos/', blogviews.blog_overview, {'category': 'Aktuelles'}, name='blog_page'),
               path('infos/seite/<int:page>/', blogviews.blog_overview, {'category': 'Aktuelles'},
                    name='blog_page'),
               path('infos/<slug:slug>/', blogviews.post, name='blog_detail'),
               path('infos/neu/', blogviews.PostCreate.as_view(), name='blog_post_add'),
               path('infos/bearbeiten/<int:pk>/', blogviews.PostUpdate.as_view(), name='blog_post_change'),
               path('infos/entfernen/<int:pk>/', blogviews.PostDelete.as_view(), name='blog_post_delete'),
               path('intern/themen/', blogviews.blog_overview, {'category': 'Themen'}, name='blog_themen'),
               path('intern/arbeitskreis/mitglieder/', pageviews.page,
                    {'url': '/intern/arbeitskreis/mitglieder/'},
                    name='arbeitskreis_mitglieder'),
               path('intern/bundesgilde/', pageviews.page, {'url': '/intern/bundesgilde/'}, name='bundesgilde'),

               path('heimabende/', include('evening_program.urls')),
               path('karten/',
                    view=lambda _: HttpResponsePermanentRedirect('https://karte.deutscher-pfadfinderbund.de')),

               path('admin/', admin.site.urls),
               path('accounts/', include('allauth.urls')),
               path('', include('django.contrib.auth.urls')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    path('impressum/', pageviews.page, {'url': '/impressum/'}, name='impressum'),
    path('datenschutz/', pageviews.page, {'url': '/datenschutz/'}, name='datenschutz'),
    path('arbeitskreis/', pageviews.page, {'url': '/arbeitskreis/'}, name='arbeitskreis'),

    path('kontakt/', pageviews.page, {'url': '/kontakt/'}, name='kontakt'),

    re_path(r'^(?P<url>.*/)$', pageviews.page, name='page'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
