# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from filer.models import File
from filer.models import Folder


@login_required
def documents(request):
    files = File.objects.all()
    folders = Folder.objects.all()
    #print(files[0])
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})