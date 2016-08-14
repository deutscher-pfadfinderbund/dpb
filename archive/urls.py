from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'katalog/$', views.search, name='search'),
    url(r'einschicken/$', views.send_in, name='send_in'),
]
