from django.conf.urls import url

from . import views

app_name = 'evening_program'

urlpatterns = [
    url(r'^$', views.evening_program, name='index'),
    url(r'^neu/$', views.ProgramCreate.as_view(success_url='/heimabende'), name='add'),
    url(r'^(?P<slug>[\w-]+)/$', views.evening_program_details, name='details'),
]
