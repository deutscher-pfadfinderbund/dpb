from django.urls import path

from . import views

app_name = "vorfreude"

urlpatterns = [
    path("", views.index, name="index")
]
