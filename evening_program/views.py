# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Program


@login_required
def evening_program(request):
    programs = Program.objects.all().order_by("title")
    return render(request, "evening_program/index.html", {"programs": programs})


@login_required
def evening_program_details(request, slug):
    program = Program.objects.get(slug=slug)
    return render(request, "evening_program/details.html", {"program": program})


class ProgramCreate(LoginRequiredMixin, CreateView):
    model = Program
    fields = ["title", "target", "preparation", "execution", "greatness", "contact_name", "contact_group",
              "contact_mail", "file1", "file2", "file3"]
