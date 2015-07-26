# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from filer.models import File
from filer.models import Folder


@login_required
def documents(request):
    files = File.objects.all().order_by("-modified_at")
    folders = Folder.objects.all().order_by("-name")
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})