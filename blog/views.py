from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from .models import Post, Category


@login_required
def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/post.html', {'post': post})


@login_required
def current_overview(request):
    try:
        category = Category.objects.filter(name="Aktuelles")
        posts = pack(Post.objects.filter(
            Q(category=category[0].id),
            Q(public=True),
            Q(archive=False),
        ))
    except Post.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'blog/list.html',
                  {'posts': posts,
                   'heading': "Aktuelles",
                   'intro': "Hier gibt es eine Übersicht aktueller Beiträge rund um den DPB."})


@login_required
def topics(request, slug):
    pass


################################ Aux functions

def pack(_list):
    nlist = list(_list)
    if len(nlist) % 2:      # Append none if len is odd
        nlist.append(None)
    return zip(nlist[::2], nlist[1::2])