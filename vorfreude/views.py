from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic.edit import CreateView

from vorfreude.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ["fahrtenname", "foto", "gilde", "bundesgruppe", "gedanken", "sagen"]


def index(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "vorfreude/index.html", {"posts": posts})
