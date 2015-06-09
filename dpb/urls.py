from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views as flatpageviews
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^bundesarchiv/', include('archive.urls', namespace='archive')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
    url(r'^accounts/', include('login.urls', namespace='login')),
    url(r'^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^impressum/$', flatpageviews.flatpage, {'url': '/impressum/'}, name='impressum'),
    url(r'^kontakt/$', flatpageviews.flatpage, {'url': '/kontakt/'}, name='kontakt'),
    url(r'^geschichte/$', flatpageviews.flatpage, {'url': '/geschichte/'}, name='geschichte'),
    url(r'^bundesordnung/$', flatpageviews.flatpage, {'url': '/bundesordnung/'}, name='bundesordnung'),
    url(r'^was-sind-pfadfinder/$', flatpageviews.flatpage, {'url': '/was-sind-pfadfinder/'}, name='was-sind-pfadfinder'),
    url(r'^(?P<url>.*/)$', flatpageviews.flatpage, name='flatpage'),
]