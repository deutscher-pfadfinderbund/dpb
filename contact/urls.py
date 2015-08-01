from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import contact


urlpatterns = [
    # Form URLs
    url(r'^$', contact),
    url(r'^verschickt/$', TemplateView.as_view(template_name='contact/verschickt.html'), name='verschickt'),
]
