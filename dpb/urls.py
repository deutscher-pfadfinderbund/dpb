from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^bundesarchiv/', include('archive.urls', namespace='archive')),
    url(r'^pages/', include('django.contrib.flatpages.urls', namespace='pages')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
    url(r'^accounts/', include('login.urls', namespace='login')),
    url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Short URLs for Flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^geschichte/$', 'flatpage', {'url': '/geschichte/'}, name='geschichte'),
    url(r'^was-sind-pfadfinder/$', 'flatpage', {'url': '/was-sind-pfadfinder/'}, name='was-sind-pfadfinder'),
    url(r'^bundesordnung/$', 'flatpage', {'url': '/bundesordnung/'}, name='bundesordnung'),
)
