from django.conf.urls import url

from . import views

app_name = 'permalink'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.redirectPermanent),
]
