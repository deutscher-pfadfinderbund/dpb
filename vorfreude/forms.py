from django.forms import ModelForm

from vorfreude.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["created", "modified"]
