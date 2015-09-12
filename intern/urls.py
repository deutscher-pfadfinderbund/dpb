from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dokumente/$', views.documents, name='documents'),
    url(r'termine/$', views.dates, name='dates'),
    url(r'termine/(?P<id>[0-9]+)/$', views.date_detail, name='date_detail'),
]