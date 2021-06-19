from django.urls import path

from . import views

app_name = "adressverzeichnis"

urlpatterns = [
    path("", views.index, name="index")
]
