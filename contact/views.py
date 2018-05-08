from datetime import datetime

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from dpb.settings import EMAIL_RECIPIENT
from .forms import EmailForm


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            author = str(cd["firstname"] + " " + cd["lastname"])
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
                cd.get('email', EMAIL_RECIPIENT),
                [EMAIL_RECIPIENT],
            )
            return HttpResponseRedirect('/kontakt/verschickt/')
    else:
        form = EmailForm()
    return render(request, 'contact/email.html', {'form': form})
