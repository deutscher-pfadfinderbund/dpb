from django.urls import re_path

from . import views

app_name = 'intern'

urlpatterns = [
    re_path(r'arbeitskreis/$', views.work_group, name='arbeitskreis'),
    re_path(r'dokumente/$', views.documents, name='documents'),

    re_path(r'haeuser/$', views.houses, name='houses'),
    re_path(r'haeuser/neu/$', views.house_add, name='house_add'),
    re_path(r'haeuser/(?P<slug>[\w-]+)/$', views.house_detail, name='house_detail'),

    re_path(r'segeln/$', views.sailing, name='sailing'),
    re_path(r'segeln/kommentare-aus-dem-DPB$', views.sailing_comments, name='sailing_comments'),
    re_path(r'segeln/interview-mit-dem-falado-ev$', views.sailing_interview_falado, name='sailing_interview_falado'),

    re_path(r"kalender/$", views.calendar, name='calendar'),
]
