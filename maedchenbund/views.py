from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Document


@login_required
def documents(request):
    docs = Document.objects.all().order_by("title")
    return render(request, 'home.html', {'documents': docs})
