from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Post, Category


@login_required
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})


class PostCreate(PermissionRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("blog_page")
    permission_required = "blog.can_edit"


class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("blog_page")
    permission_required = "blog.can_edit"


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog_page")
    permission_required = "blog.can_edit"


@login_required
def blog_overview(request, page=1, category="Aktuelles"):
    category = get_object_or_404(Category, name=category)
    all_posts = Post.objects.filter(
        Q(category=category),
        Q(public=True),
        Q(archive=False),
    ).select_related("author").order_by("-created")

    paginator = Paginator(all_posts, 6)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html',
                  {'posts': pack(posts),
                   'paginator': posts,
                   'length': range(len(posts)),
                   'category': category})


# Aux functions

def pack(_list):
    nlist = list(_list)
    if len(nlist) % 2:  # Append none if len is odd
        nlist.append(None)
    return zip(nlist[::2], nlist[1::2])
