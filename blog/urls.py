from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^aktuelles/(?P<slug>[\w-]+)/$', views.current),
    url(r'^themen/(?P<slug>[\w-]+)/$', views.topics),
]
