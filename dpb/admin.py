from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from tinymce.widgets import TinyMCE

from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageForm)