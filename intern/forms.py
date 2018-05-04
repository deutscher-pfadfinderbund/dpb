from django.forms import ModelForm

from .models import House


class HouseForm(ModelForm):
    class Meta:
        model = House
        exclude = []
