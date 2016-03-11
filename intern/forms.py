from captcha.fields import ReCaptchaField
from django.forms import ModelForm
from .models import House


class HouseForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = House
        exclude = []
