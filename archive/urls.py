from django.urls import path

from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.search, name='search'),
    path('katalog/<int:pk>', views.detail, name='details'),
    path('einschicken/', views.send_in, name='send_in'),
    path('feedback/', views.feedback, name='feedback_abschicken'),
    path('feedback/danke/', views.feedback_danke, name='feedback_erfolgreich'),
]
