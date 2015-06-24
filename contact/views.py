from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import EmailForm


RECIPIENTS = ["cmeter@gmail.com"]


def sendmail(request):
    if request.method == 'POST':
        print("POST")
        form = EmailForm(request.POST)
        if form.is_valid():
            print("IS VALID")
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            botcheck = form.cleaned_data['botcheck'].lower()
            message = form.cleaned_data['message']
            if botcheck == 'ja':
                print("botcheck ja")
                try:
                    #print("send mail to " + RECIPIENTS[0])
                    #fullemail = firstname + " " + lastname + " " + "<" + email + ">"
                    send_mail(subject, message, email, RECIPIENTS)
                    return HttpResponseRedirect('/email/verschickt/')
                except:
                    print("catch")
                    return HttpResponseRedirect('/email/')
        else:
            print("invalid form")
            return HttpResponseRedirect('/email/')
    else:
        print("pos 2")
        return HttpResponseRedirect('/email/')  
