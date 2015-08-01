from django.http import Http404
from django.shortcuts import render
from .models import Post


def current(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/post.html', {'post': post})


def topics(request, slug):
    pass