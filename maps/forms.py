from django.forms import ModelForm
from .models import GroupMaps


class GroupMapsForm(ModelForm):
    class Meta:
        model = GroupMaps
        exclude = []
