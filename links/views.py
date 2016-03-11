from django.shortcuts import render

from .models import Link, LinkCategory


def links(request):
    links = Link.objects.all().order_by("state")
    states = set()
    for link in links:
        try:
            states.add(link.state)
        except ValueError:
            pass
    cats = LinkCategory.objects.all().order_by("name")
    return render(request, 'links.html', {'links': links,
                                          'cats': cats,
                                          'states': states})
