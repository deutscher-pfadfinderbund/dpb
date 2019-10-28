from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, QuerySet
from django.forms import ModelForm
from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView

from archive.forms import FeedbackForm
from blog.models import Post, Category
from .models import Item, Feedback

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


def _remove_blocked_items(items: QuerySet) -> QuerySet:
    return items.filter(reviewed=True).filter(active=True)


def _search_fulltext(items, query):
    """
    Given a query, search complete database
    """
    try:
        # Specify which fields are searchable
        items = items.filter(  # '|' = OR; ',' = AND
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
        return _remove_blocked_items(items)
    except Item.DoesNotExist:
        return items


def _search_extended(items, title, author, keyword, mediatype="alle", doctype="alle"):
    """
    If there are any additional search keywords provided, concatenate them with AND and return the result.
    """
    try:
        if mediatype and len(mediatype) > 0 and mediatype != "alle":
            items = items.filter(medartanalog=mediatype)
        if doctype and len(doctype) > 0 and doctype != "alle":
            items = items.filter(doctype=doctype)
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


class ItemCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['sent_in_by'].required = True

    class Meta:
        model = Item
        fields = (
            "title", "medartanalog", "doctype", "collection", "author", "year", "place", "amount", "notes", "file",
            "file2", "file3", "sent_in_by")
        exclude = ("modified", "pub_date", "crossreference", "source", "keywords",
                   "location", "active", "reviewed", "owner", "signature", "date")

        help_texts = {"sent_in_by": "Dein Name und/oder E-Mail Adresse. Bspw.: Fahrtenname, fahrtenname@hotmail.com"}


class ItemCreate(CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse('archive:search')


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
    title = _parse_form_field(request, "titel")
    author = _parse_form_field(request, "autor")
    keyword = _parse_form_field(request, "schlagwort")
    mediatype = _parse_form_field(request, "medientyp")
    doctype = _parse_form_field(request, "dokumenttyp")

    lengths = len(query) + len(title) + len(author) + len(keyword)

    if lengths >= MINIMUM_LENGTH_OF_QUERY:
        items = _search_fulltext(items, query)
        items = _search_extended(items, title, author, keyword, mediatype, doctype)
        results = _remove_blocked_items(items.order_by('title'))
    elif 0 < lengths < MINIMUM_LENGTH_OF_QUERY:
        errors = True
        results = None

    results = results if results and results is not [] else None

    return render(request, 'archive/search.html', {
        "results": results,
        "query": query,
        "title": title,
        "author": author,
        "keyword": keyword,
        "mediatype": mediatype,
        "doctype": doctype,
        "errors": errors,
        "min_length_of_query": MINIMUM_LENGTH_OF_QUERY,
        "mediatypes": Item.medartanalog_choices,
        "doctypes": Item.doctype_choices
    })


@login_required()
def detail(request: HttpRequest, pk: Item):
    item = get_object_or_404(Item, pk=pk, active=True, reviewed=True)
    return render(request, "archive/detail.html", {
        "item": item,
        "feedback_form": FeedbackForm()
    })


@login_required()
def feedback(request: HttpRequest):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        item = request.POST.get('item')
        if form.is_valid() and item is not None:
            form.cleaned_data['item'] = Item.objects.get(id=item)
            Feedback(**form.cleaned_data).save()
            return HttpResponseRedirect(reverse('archive:feedback_erfolgreich'))
    return HttpResponseRedirect(reverse('archive:search'))


@login_required()
def feedback_danke(request: HttpRequest):
    return render(request, 'archive/feedback_danke.html')
