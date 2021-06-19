"""
Endlich ein modernes Adressverzeichnis für unseren Bund!
"""
from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "adressverzeichnis/index.html")
