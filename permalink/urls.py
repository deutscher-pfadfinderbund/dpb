from django.urls import path

from . import views

app_name = 'permalink'

urlpatterns = [
    path('<slug>/', views.redirectPermanent, name='redirectPermanent')
]
