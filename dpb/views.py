import datetime

from django.utils import timezone
from django.shortcuts import render
from django.views import generic

from blog.models import Post


def index(request):
    now = timezone.now()
    one_year_ago = now - datetime.timedelta(days=365)
    news = Post.objects.filter(
        created__range=(one_year_ago, now)
    ).order_by('-created')[:3]
    return render(request, 'index.html', {'news': news})


class BundesordnungView(generic.ListView):
    template_name = 'bundesordnung.html'
    context_object_name = ''

    def get_queryset(self):
        return None


class DPBView(generic.ListView):
    template_name = 'dpb.html'
    context_object_name = ''

    def get_queryset(self):
        return None


class PfadfinderView(generic.ListView):
    template_name = 'pfadfinder.html'
    context_object_name = ''

    def get_queryset(self):
        return None
