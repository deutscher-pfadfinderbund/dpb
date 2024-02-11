from django.urls import re_path
from django.views.generic.base import TemplateView

from .views import contact

app_name = 'email'

urlpatterns = [
    # Form URLs
    re_path(r'^$', contact),
    re_path(r'^verschickt/$', TemplateView.as_view(template_name='contact/verschickt.html'), name='verschickt'),
]
