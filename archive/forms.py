from django.forms import ModelForm
from pagedown.forms import PagedownField
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        widgets = {
            'name': PagedownField()
        }
