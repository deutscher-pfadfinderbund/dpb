from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q

from .models import Item


def index(request):
    req = request.GET.get('q')
    query = None
    results = None
    if req:
        query = req
    else:
        query = ""
    try:
        query = str(query)
    except ValueError:
        query = ""
    if query:
        try:
            # Specify which fields are searchable
            results = Item.objects.filter(
                Q(title__iexact=query) |        # '|' = OR; ',' = AND
                Q(signature__iexact=query)).exclude(public=False)
        except Item.DoesNotExist:
            results = None
    context = RequestContext(request)
    return render_to_response('archive/index.html', {"results": results, "query": query}, context_instance=context)
