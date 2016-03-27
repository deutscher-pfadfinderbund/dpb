from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Post, Category


@login_required
def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Dieser Beitrag konnte leider nicht gefunden werden.")
    return render(request, 'blog/post.html', {'post': post})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("blog_page")


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("blog_page")


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog_page")


@login_required
def blog_overview(request, page=1, category="Aktuelles"):
    try:
        category = Category.objects.filter(name=category)
        all_posts = Post.objects.filter(
            Q(category=category[0].id),
            Q(public=True),
            Q(archive=False),
        ).order_by("-created")

        paginator = Paginator(all_posts, 6)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)
    except Post.DoesNotExist:
        raise Http404("Diese Beiträge konnten leider nicht gefunden werden.")
    return render(request, 'blog/list.html',
                  {'posts':     pack(posts),
                   'paginator': posts,
                   'length':    range(len(posts)),
                   'category':  category[0]})




################################ Aux functions

def pack(_list):
    nlist = list(_list)
    if len(nlist) % 2:      # Append none if len is odd
        nlist.append(None)
    return zip(nlist[::2], nlist[1::2])