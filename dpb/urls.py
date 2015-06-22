from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

from pages import views as pageviews

urlpatterns = [
    # Hard-coded pages
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^bundesordnung/$', views.BundesordnungView.as_view(), name='bundesordnung'),
    url(r'^dpb/$', views.DPBView.as_view(), name='dpb'),

    # Apps
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^bundesarchiv/', include('archive.urls', namespace='archive')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
    url(r'^accounts/', include('login.urls', namespace='login')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^impressum/$', pageviews.page, {'url': '/impressum/'}, name='impressum'),
    url(r'^kontakt/$', pageviews.page, {'url': '/kontakt/'}, name='kontakt'),
    url(r'^geschichte/$', pageviews.page, {'url': '/geschichte/'}, name='geschichte'),
    url(r'^was-sind-pfadfinder/$', pageviews.page, {'url': '/was-sind-pfadfinder/'}, name='was-sind-pfadfinder'),

    url(r'^test/$', pageviews.page, {'url': '/test/'}, name='test'),

    url(r'^(?P<url>.*/)$', pageviews.page, name='page'),
]