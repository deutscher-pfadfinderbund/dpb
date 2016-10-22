from django.shortcuts import render
from django.db.models import Q

from .models import Feedback
from .forms import FeedbackForm


def index(request):
    feedbacks = Feedback.objects.order_by('-created').filter(Q(public=True))
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/danke.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form, 'feedbacks': feedbacks})
