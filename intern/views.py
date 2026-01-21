# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from filer.models import File, Folder

from .forms import HouseForm
from .models import House


@login_required
def documents(request):
    files = File.objects.all().order_by("-modified_at")
    folders = Folder.objects.all()
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})


@login_required
def houses(request):
    houses = House.objects.all().order_by("name")
    return render(request, 'intern/houses.html', {'houses': houses})


@login_required
def house_add(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'intern/house_success.html', {"form": form})
        return render(request, 'intern/house_add.html', {"form": form})
    else:
        form = HouseForm()
    return render(request, 'intern/house_add.html', {'form': form})


@login_required
def house_detail(request, slug):
    house = get_object_or_404(House, slug=slug)
    return render(request, 'intern/house_detail.html', {'house': house})


# Sailing
@login_required
def sailing(request):
    return render(request, 'intern/sailing_home.html')


@login_required
def sailing_comments(request):
    return render(request, 'intern/sailing_comments.html')


@login_required
def sailing_interview_falado(request):
    return render(request, 'intern/sailing_interview_falado.html')


# Calender
@login_required
def calendar(request):
    return render(request, 'intern/calendar.html')
