from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Feedback
from .forms import FeedbackForm

def index(request):
    feedbacks = Feedback.objects.order_by('-created')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/danke.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form, 'feedbacks': feedbacks})