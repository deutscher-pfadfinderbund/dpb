import itertools

from django import forms
from tinymce.widgets import TinyMCE
from django.utils.text import slugify

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = '__all__'