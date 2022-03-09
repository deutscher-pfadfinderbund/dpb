from django.views.generic.edit import CreateView

from vorfreude.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ["fahrtenname", "foto", "gilde", "bundesgruppe", "gedanken", "sagen"]
