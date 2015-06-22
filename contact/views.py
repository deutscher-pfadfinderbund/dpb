from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import EmailForm


RECIPIENT = "cmeter@gmail.com"


def sendmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            botcheck = form.cleaned_data['botcheck'].lower()
            message = form.cleaned_data['message']
            if botcheck == 'yes':
                try:
                    fullemail = firstname + " " + lastname + " " + "<" + email + ">"
                    send_mail(subject, message, fullemail, [RECIPIENT])
                    return HttpResponseRedirect('/email/thankyou/')
                except:
                    return HttpResponseRedirect('/email/')
        else:
            return HttpResponseRedirect('/email/')
    else:
        return HttpResponseRedirect('/email/')  
