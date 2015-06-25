from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import sendmail


urlpatterns = [
    # Form URLs
    url(r'^send/$', sendmail),
    url(r'^verschickt/$', TemplateView.as_view(template_name='contact/verschickt.html'), name='verschickt'),
    url(r'^$', TemplateView.as_view(template_name='contact/email.html'), name='email'),
]
