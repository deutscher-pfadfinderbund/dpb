from django.conf.urls import url

from . import views

app_name = 'maps'

urlpatterns = [
    url(r'^$', views.groupmaps, name='index'),
    url(r'^neu/$', views.add, name='add'),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name='details'),
]
