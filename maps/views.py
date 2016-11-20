from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import GroupMaps
from .forms import GroupMapsForm


@login_required
def groupmaps(request):
    maps = GroupMaps.objects.all().order_by("group")
    return render(request, "groupmaps.html", {"maps": maps})


@login_required
def add(request):
    if request.method == 'POST':
        form = GroupMapsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "groupmaps_success.html", {"form": form})
        return render(request, "groupmaps_add.html", {"form": form})
    else:
        form = GroupMapsForm()
    return render(request, "groupmaps_add.html", {"form": form})


@login_required
def details(request, slug):
    map = GroupMaps.objects.get(slug=slug)
    return render(request, "groupmaps_details.html", {"map": map})
