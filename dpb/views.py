import datetime
from django.shortcuts import render
from django.views import generic
from blog.models import Post


def index(request):
    news = Post.objects.filter(created__lte=datetime.datetime.today(), created__gt=datetime.datetime.today()-datetime.timedelta(days=365)).order_by('-created')[:3]
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