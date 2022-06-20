import os
from datetime import datetime

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmailForm


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if cd["honeypot"]:
                return HttpResponseRedirect('/kontakt')

            author = str(cd["name"])
            subject = str("[DPB Homepage] " + cd['subject'])
            message = """\
Kontaktanfrage über www.deutscher-pfadfinderbund.de

Von: {}
Betreff: {}
Zeit: {}

Nachricht:
{}
            """.format(author, cd['subject'], datetime.now(), cd['message'])

            send_mail(
                subject,
                message,
                cd.get('email', os.getenv("EMAIL_RECIPIENT", "cmeter@googlemail.com")),
                [os.getenv("EMAIL_RECIPIENT", "cmeter@googlemail.com")],
            )
            return HttpResponseRedirect('/kontakt/verschickt/')
    else:
        form = EmailForm()
    return render(request, 'contact/email.html', {'form': form})
