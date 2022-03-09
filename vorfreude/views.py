from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from vorfreude.forms import PostForm
from vorfreude.models import Post


def index(request: HttpRequest, success: bool = False):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post(**form.cleaned_data).save()
            return HttpResponseRedirect(reverse('vorfreude:index', args=(True,)))
    return render(request, "vorfreude/index.html", {"posts": posts,
                                                    "post_form": PostForm(),
                                                    "success": success})
