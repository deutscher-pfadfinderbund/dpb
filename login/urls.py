from django.conf.urls import url
from login.views import *


urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'), # If user is not login it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success),
]
