# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def evening_program(request):
    return render(request, 'evening_program/index.html')