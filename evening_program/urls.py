from django.urls import re_path

from . import views

app_name = 'evening_program'

urlpatterns = [
    re_path(r'^$', views.evening_program, name='index'),
    re_path(r'^neu/$', views.ProgramCreate.as_view(success_url='/heimabende'), name='add'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.evening_program_details, name='details'),
]
