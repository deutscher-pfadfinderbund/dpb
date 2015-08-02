from django.http import Http404
from django.shortcuts import render
from .models import Post, Category


def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/post.html', {'post': post})


def current_overview(request):
    try:
        category = Category.objects.filter(name="Aktuelles")
        posts = pack(Post.objects.filter(category=category[0].id))
    except Post.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'blog/list.html',
                  {'posts': posts,
                   'heading': "Aktuelles",
                   'intro': "Hier gibt es eine Übersicht aktueller Beiträge rund um den DPB."})


def topics(request, slug):
    pass


################################ Aux functions

def pack(_list):
    new_list = zip(_list[::2], _list[1::2])
    if len(_list) % 2:
        new_list.append((_list[-1], None))
    return new_list