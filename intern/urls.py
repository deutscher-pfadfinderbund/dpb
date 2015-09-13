from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dokumente/$', views.documents, name='documents'),
    url(r'termine/$', views.dates, name='dates'),
    url(r'termine/(?P<id>[0-9]+)/$', views.date_detail, name='date_detail'),
    url(r'haeuser/$', views.houses, name='houses'),
    url(r'haeuser/(?P<id>[0-9]+)/$', views.house_detail, name='house_detail'),
]