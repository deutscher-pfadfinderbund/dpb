from django.urls import path

from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.search, name='search'),
    path('katalog/<int:pk>', views.detail, name='details'),
    path('einschicken/', views.send_in, name='send_in'),
]
