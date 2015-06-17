from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<url>.*)$', views.page, name='pages'),
]
