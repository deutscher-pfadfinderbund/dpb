from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dokumente/$', views.documents, name='documents'),
]