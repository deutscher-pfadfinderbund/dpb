from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Item

@login_required
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
            results = Item.objects.filter(      # '|' = OR; ',' = AND
                Q(signature__iexact=query) |
                Q(author__iexact=query) |
                Q(title__iexact=query) |
                Q(date__iexact=query) |
                Q(year__iexact=query) |
                Q(place__iexact=query) |
                Q(doctype__iexact=query) |
                Q(medartdig__iexact=query) |
                Q(medartanalog__iexact=query) |
                Q(keywords__iexact=query) |
                Q(location__iexact=query) |
                Q(source__iexact=query) |
                Q(notes__iexact=query) |
                Q(collection__iexact=query) |
                Q(amount__iexact=query) |
                Q(crossreference__iexact=query) |
                Q(active__iexact=query) |
                Q(reviewed__iexact=query) |
                Q(owner__iexact=query) |
                Q(pub_date__iexact=query)
            ).exclude(active=False).exclude(reviewed=False)
        except Item.DoesNotExist:
            results = None
    context = RequestContext(request)
    return render_to_response('archive/index.html', {"results": results, "query": query}, context_instance=context)
