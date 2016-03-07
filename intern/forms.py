from django.forms import ModelForm
from pagedown.forms import PagedownField
from .models import House


class HouseForm(ModelForm):
    class Meta:
        model = House
        widgets = {
            'name': PagedownField()
        }
