from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from blog import views as blogviews
from pages import views as pageviews
from . import views

urlpatterns = [
    # Hard-coded pages
    url(r'^$', views.index, name='index'),
    url(r'^bundesordnung/$', views.BundesordnungView.as_view(), name='bundesordnung'),
    url(r'^dpb/$', views.DPBView.as_view(), name='dpb'),
    url(r'^pfadfinder/$', views.PfadfinderView.as_view(), name='pfadfinder'),

    # Apps
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^bundesarchiv/', include('archive.urls', namespace='archive')),
    url(r'^kontakt/', include('contact.urls', namespace='email')),
    url(r'^links/', include('links.urls', namespace='links')),
    url(r'^filer/', include('filer.urls')),

    # Members Area
    url(r'^intern/', include('intern.urls', namespace='intern')),
    url(r'^infos/$', blogviews.blog_overview, {'category': 'Aktuelles'}, name='blog_page'),
    url(r'^infos/seite/(?P<page>[0-9]+)/$', blogviews.blog_overview, {'category': 'Aktuelles'}, name='blog_page'),
    url(r'^infos/(?P<slug>[\w-]+)/$', blogviews.post, name='blog_detail'),
    url(r'^infos/neu/$', blogviews.PostCreate.as_view(), name='blog_post_add'),
    url(r'^infos/bearbeiten/(?P<pk>[0-9]+)/$', blogviews.PostUpdate.as_view(), name='blog_post_change'),
    url(r'^infos/entfernen/(?P<pk>[0-9]+)/$', blogviews.PostDelete.as_view(), name='blog_post_delete'),
    url(r'^intern/themen/$', blogviews.blog_overview, {'category': 'Themen'}, name='blog_themen'),
    url(r'^intern/arbeitskreis/mitglieder/$', pageviews.page, {'url': '/intern/arbeitskreis/mitglieder/'},
        name='arbeitskreis_mitglieder'),
    url(r'^intern/bundesgilde/$', pageviews.page, {'url': '/intern/bundesgilde/'}, name='bundesgilde'),

    url(r'^heimabende/', include('evening_program.urls', namespace='evening_program')),
    url(r'^karten/', include('maps.urls', namespace='maps')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
    url(r'^accounts/', include('login.urls', namespace='login')),
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
