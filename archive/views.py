from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Item


def parse_form_field(request, param):
    """
    Parse parameter from request and return empty string if not provided or not parsable.

    :param request:
    :param param: to be parsed
    :return: str
    """
    req = request.GET.get(param)
    query = ""
    if req:
        query = req
    try:
        query = str(query)
    except ValueError:
        query = ""
    return query


def search_fulltext(items, query):
    """
    Given a query, search complete database

    :param query:
    :return:
    """
    try:
        # Specify which fields are searchable
        return items.filter(  # '|' = OR; ',' = AND
            Q(signature__icontains=query) |
            Q(author__icontains=query) |
            Q(title__icontains=query) |
            Q(date__icontains=query) |
            Q(year__icontains=query) |
            Q(place__icontains=query) |
            Q(doctype__icontains=query) |
            Q(medartanalog__icontains=query) |
            Q(keywords__icontains=query) |
            Q(location__icontains=query) |
            Q(source__icontains=query) |
            Q(notes__icontains=query) |
            Q(collection__icontains=query) |
            Q(amount__icontains=query) |
            Q(crossreference__icontains=query) |
            Q(active__icontains=query) |
            Q(reviewed__icontains=query) |
            Q(owner__icontains=query) |
            Q(pub_date__icontains=query)
        )
    except Item.DoesNotExist:
        return items


def search_extended(items, title, author, keyword, doctype):
    """
    If there are any additional search keywords provided, concatenate them with AND and return the result.

    :param title:
    :param author:
    :param keyword:
    :param doctype:
    :return:
    """
    queried = False
    try:
        if title and len(title) != 0:
            queried = True
            items = items.filter(Q(title__icontains=title))
        if author and len(author) != 0:
            queried = True
            items = items.filter(Q(author__icontains=author))
        if keyword and len(keyword) != 0:
            queried = True
            items = items.filter(keyword__icontains=keyword)
        if queried:
            return items
    except Item.DoesNotExist:
        return None


@login_required
def index(request):
    title = author = keyword = doctype = results = None
    items = Item.objects.exclude(active=False)

    query = parse_form_field(request, "q")
    title = parse_form_field(request, "title")
    author = parse_form_field(request, "author")
    keyword = parse_form_field(request, "keyword")
    doctype = parse_form_field(request, "doctype")

    items = search_fulltext(items, query)
    results = search_extended(items, title, author, keyword, doctype)

    context = RequestContext(request)

    return render_to_response('archive/index.html', {"results": results,
                                                     "query": query,
                                                     "title": title,
                                                     "author": author,
                                                     "keyword": keyword,
                                                     "doctype": doctype}, context_instance=context)
