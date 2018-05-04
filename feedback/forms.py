from django.forms import ModelForm

from feedback.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'note']
