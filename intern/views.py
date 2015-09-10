# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from filer.models import File, Folder
from .models import Date


@login_required
def documents(request):
    files = File.objects.all().order_by("-modified_at")
    folders = Folder.objects.all()
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})

@login_required
def dates(request):
    dates = Date.objects.all().order_by("-date")
    return render(request, 'intern/dates.html', {'dates': dates})