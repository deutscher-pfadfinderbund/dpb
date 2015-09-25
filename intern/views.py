# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from filer.models import File, Folder
from .models import Date, House


@login_required
def documents(request):
    files = File.objects.all().order_by("-modified_at")
    folders = Folder.objects.all()
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})


@login_required
def dates(request):
    dates = Date.objects.all().order_by("-start")
    return render(request, 'intern/dates.html', {'dates': dates})


@login_required
def date_detail(request, id):
    date = Date.objects.get(id=id)
    return render(request, 'intern/date_detail.html', {'date': date})


@login_required
def houses(request):
    houses = House.objects.all().order_by("-name")
    return render(request, 'intern/houses.html', {'houses': houses})


@login_required
def house_detail(request, id):
    house = House.objects.get(id=id)
    return render(request, 'intern/house_detail.html', {'house': house})