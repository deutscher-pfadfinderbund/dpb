from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q

from .models import Item


def index(request):
    query = request.GET.get('q')
    results = None
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            # Query comes here!
            results = Item.objects.filter(title__contains=query).values()
        except Item.DoesNotExist:
            results = None
    context = RequestContext(request)
    return render_to_response('archive/index.html', {"results": results, "query": query}, context_instance=context)
