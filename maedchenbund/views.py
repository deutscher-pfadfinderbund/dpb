from django.shortcuts import render

from .models import Document


def documents(request):
    docs = Document.objects.all().order_by("title")
    return render(request, 'home.html', {'documents': docs})
