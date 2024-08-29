from django.urls import re_path

from . import views

app_name = 'permalink'

urlpatterns = [
    re_path(r'^<slug:slug>/$', views.redirectPermanent),
]
