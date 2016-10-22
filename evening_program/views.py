# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Program


@login_required
def evening_program(request):
    programs = Program.objects.all().order_by("title")
    return render(request, "evening_program/index.html", {"programs": programs})
