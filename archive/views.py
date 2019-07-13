from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import render

from blog.models import Post, Category
from .models import Item

MINIMUM_LENGTH_OF_QUERY = 4


def _parse_form_field(request: HttpRequest, param: str) -> str:
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


def _search_fulltext(items, query):
    """
    Given a query, search complete database
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


def _search_extended(items, title, author, keyword, doctype):
    """
    If there are any additional search keywords provided, concatenate them with AND and return the result.

    :param items: Potentially filtered collection of all items
    :param title:
    :param author:
    :param keyword:
    :param doctype:
    :return:
    """
    try:
        if title and len(title) != 0:
            items = items.filter(Q(title__icontains=title))
        if author and len(author) != 0:
            items = items.filter(Q(author__icontains=author))
        if keyword and len(keyword) != 0:
            items = items.filter(keywords__icontains=keyword)
        return items
    except Item.DoesNotExist:
        return None


@login_required
def index(request):
    try:
        category = Category.objects.filter(name="Bundesarchiv")
        if len(category) == 0:
            posts = None
        else:
            posts = Post.objects.filter(
                Q(category=category[0].id),
                Q(public=True),
                Q(archive=False),
            ).order_by("-created")
    except Post.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'archive/index.html', {"posts": posts})


@login_required
def send_in(request):
    return render(request, 'archive/send_in.html')


def _paginate_results(items, page):
    paginator = Paginator(items, 20)
    try:
        prepared_items = paginator.page(page)
    except PageNotAnInteger:
        prepared_items = paginator.page(1)
    except EmptyPage:
        prepared_items = paginator.page(paginator.num_pages)
    return prepared_items


@login_required
def search(request):
    items = Item.objects.exclude(active=False)
    errors = False
    results = []

    query = _parse_form_field(request, "q")
    title = _parse_form_field(request, "title")
    author = _parse_form_field(request, "author")
    keyword = _parse_form_field(request, "keyword")
    doctype = _parse_form_field(request, "doctype")

    lengths = len(query) + len(title) + len(author) + len(keyword) + len(doctype)

    if lengths >= MINIMUM_LENGTH_OF_QUERY:
        items = _search_fulltext(items, query)
        items = _search_extended(items, title, author, keyword, doctype)
        results = items.order_by('title')
    elif 0 < lengths < MINIMUM_LENGTH_OF_QUERY:
        errors = True
        results = None

    results = results if results and results is not [] else None

    return render(request, 'archive/search.html', {"results": results,
                                                   "query": query,
                                                   "title": title,
                                                   "author": author,
                                                   "keyword": keyword,
                                                   "doctype": doctype,
                                                   "errors": errors,
                                                   "min_length_of_query": MINIMUM_LENGTH_OF_QUERY})
