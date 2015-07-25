# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Q

from filer.models import File
from filer.models import Folder
from filer.models import FileManager

def documents(request):
    files = File.objects.all()
    folders = Folder.objects.all()
    #print(files[0])
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})