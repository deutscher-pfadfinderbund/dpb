from django import forms
from django.forms import ModelForm

from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        widgets = {'item': forms.HiddenInput()}
        exclude = ['archive', 'created', 'modified', 'item']
