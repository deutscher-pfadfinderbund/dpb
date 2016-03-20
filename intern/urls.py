from django.conf.urls import url

from . import views
from .views import DateCreate, DateDelete


urlpatterns = [
    url(r'arbeitskreis/$', views.work_group, name='arbeitskreis'),
    url(r'dokumente/$', views.documents, name='documents'),
    url(r'termine/$', views.dates, name='dates'),
    url(r'termine/neu/$', DateCreate.as_view(), name='date_add'),
    url(r'termine/entfernen/(?P<pk>[0-9]+)/$', DateDelete.as_view(), name='date_delete'),
    url(r'termine/(?P<id>[0-9]+)/$', views.date_detail, name='date_detail'),
    url(r'haeuser/$', views.houses, name='houses'),
    url(r'haeuser/neu/$', views.house_add, name='house_add'),
    url(r'haeuser/(?P<slug>[\w-]+)/$', views.house_detail, name='house_detail'),
]