from django.conf.urls import url

from . import views

app_name = 'links'

urlpatterns = [
    url(r'^$', views.links, name='index'),
]
