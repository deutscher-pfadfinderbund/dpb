from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

from blog import views as blogviews
from pages import views as pageviews

urlpatterns = [
    # Hard-coded pages
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^bundesordnung/$', views.BundesordnungView.as_view(), name='bundesordnung'),
    url(r'^dpb/$', views.DPBView.as_view(), name='dpb'),
    url(r'^pfadfinder/$', views.PfadfinderView.as_view(), name='pfadfinder'),

    # Apps
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^bundesarchiv/', include('archive.urls', namespace='archive')),
    url(r'^kontakt/', include('contact.urls', namespace='email')),

    # Members Area
    url(r'^intern/', include('intern.urls', namespace='intern')),
    url(r'^intern/aktuelles/$', blogviews.current_overview),
    url(r'^intern/aktuelles/(?P<slug>[\w-]+)/$', blogviews.post),
    url(r'^intern/themen/(?P<slug>[\w-]+)/$', blogviews.topics),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
    url(r'^accounts/', include('login.urls', namespace='login')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^impressum/$', pageviews.page, {'url': '/impressum/'}, name='impressum'),
    url(r'^arbeitskreis/$', pageviews.page, {'url': '/arbeitskreis/'}, name='arbeitskreis'),

    url(r'^kontakt/$', pageviews.page, {'url': '/kontakt/'}, name='kontakt'),


    url(r'^(?P<url>.*/)$', pageviews.page, name='page'),
]