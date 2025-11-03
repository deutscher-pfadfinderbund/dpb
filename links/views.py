from django.shortcuts import render

from .models import Link, LinkCategory


def links(request):
    # Optimize with select_related for foreign keys
    links = Link.objects.select_related('state', 'category').all().order_by("state")
    # Get distinct state names efficiently (values_list already optimizes the query)
    states = Link.objects.filter(state__isnull=False).values_list('state__name', flat=True).distinct()
    cats = LinkCategory.objects.all().order_by("name")
    return render(request, 'links.html', {'links': links,
                                          'cats': cats,
                                          'states': states})
