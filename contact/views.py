from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm


RECIPIENT = "cmeter@gmail.com"


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', RECIPIENT),
                [RECIPIENT],
            )
            return HttpResponseRedirect('/kontakt/verschickt/')
    else:
        form = EmailForm()
    return render(request, 'contact/email.html', {'form': form})