from django.conf.urls import url

from . import views

app_name = 'intern'

urlpatterns = [
    url(r'arbeitskreis/$', views.work_group, name='arbeitskreis'),
    url(r'dokumente/$', views.documents, name='documents'),

    url(r'haeuser/$', views.houses, name='houses'),
    url(r'haeuser/neu/$', views.house_add, name='house_add'),
    url(r'haeuser/(?P<slug>[\w-]+)/$', views.house_detail, name='house_detail'),

    url(r'segeln/$', views.sailing, name='sailing'),
    url(r'segeln/kommentare-aus-dem-DPB$', views.sailing_comments, name='sailing_comments'),
    url(r'segeln/interview-mit-dem-falado-ev$', views.sailing_interview_falado, name='sailing_interview_falado'),

    url(r"kalender/$", views.calendar, name='calendar'),
]
