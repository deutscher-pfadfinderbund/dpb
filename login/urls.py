import django.contrib.auth.views as authviews
from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', authviews.LoginView),
    url(r'^logout/$', views.logout_page),
    url(r'^login/$', authviews.LoginView),  # If user is not logged in, it will redirect to login page
    # url(r'^register/$', views.register, name='register'),
    # url(r'^register/success/$', views.register_success, name='register_success'),
]
