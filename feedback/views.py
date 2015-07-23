from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Feedback

class IndexView(generic.ListView):
    template_name = 'feedback/index.html'
    context_object_name = 'feedbacks'

    def get_queryset(self):
        """Return the last five published questions."""
        return Feedback.objects.order_by('-created')