# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from filer.models import File, Folder
from .models import Date, House
from .forms import HouseForm


def work_group(request):
    return render(request, 'intern/arbeitskreis.html')


@login_required
def documents(request):
    files = File.objects.all().order_by("-modified_at")
    folders = Folder.objects.all()
    return render(request, 'intern/documents.html', {'files': files, 'folders': folders})


@login_required
def dates(request):
    dates = Date.objects.filter(end__gte=datetime.now()).order_by("start")
    return render(request, 'intern/dates.html', {'dates': dates})


@login_required
def date_detail(request, id):
    date = Date.objects.get(id=id)
    return render(request, 'intern/date_detail.html', {'date': date})


class DateCreate(PermissionRequiredMixin, CreateView):
    model = Date
    fields = ["title", "start", "end", "location", "host", "attachment", "description"]
    permission_required = "intern.can_edit"


class DateDelete(PermissionRequiredMixin, DeleteView):
    model = Date
    success_url = reverse_lazy('intern:dates')
    permission_required = "intern.can_edit"


class DateUpdate(PermissionRequiredMixin, UpdateView):
    model = Date
    fields = ["title", "start", "end", "location", "host", "attachment", "description"]
    template_name_suffix = "_form"
    permission_required = "intern.can_edit"


@login_required
def houses(request):
    houses = House.objects.all().order_by("name")
    return render(request, 'intern/houses.html', {'houses': houses})


@login_required
def house_add(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'intern/house_success.html', {"form": form})
        return render(request, 'intern/house_add.html', {"form": form})
    else:
        form = HouseForm()
    return render(request, 'intern/house_add.html', {'form': form})


@login_required
def house_detail(request, slug):
    house = House.objects.get(slug=slug)
    return render(request, 'intern/house_detail.html', {'house': house})


# Sailing
@login_required
def sailing(request):
    return render(request, 'intern/sailing_home.html')


@login_required
def sailing_comments(request):
    return render(request, 'intern/sailing_comments.html')


@login_required
def sailing_interview_falado(request):
    return render(request, 'intern/sailing_interview_falado.html')