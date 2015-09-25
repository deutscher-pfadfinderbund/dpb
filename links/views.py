from django.shortcuts import render

from .models import Link, LinkCategory


def links(request):
    links = Link.objects.all().order_by("title")
    cats = LinkCategory.objects.all().order_by("name")
    return render(request, 'links.html', {'links': links, 'cats': cats})