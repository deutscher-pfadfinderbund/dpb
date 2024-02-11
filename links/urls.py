from django.urls import re_path

from . import views

app_name = 'links'

urlpatterns = [
    re_path(r'^$', views.links, name='index'),
]
