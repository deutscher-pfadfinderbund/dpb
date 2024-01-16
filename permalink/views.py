from django.shortcuts import get_object_or_404, redirect

from .models import Permalink


def redirectPermanent(request, slug):
    return redirect(get_object_or_404(Permalink, short=slug).redirect_url)
