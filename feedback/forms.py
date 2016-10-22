from captcha.fields import ReCaptchaField

from django.forms import ModelForm
from feedback.models import Feedback


class FeedbackForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'note']