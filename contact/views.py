from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import EmailForm


RECIPIENT = "cmeter@gmail.com"


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
            if botcheck == 'yes':
                print("botcheck yes")
                try:
                    print("send mail to " + RECIPIENT)
                    fullemail = firstname + " " + lastname + " " + "<" + email + ">"
                    send_mail(subject, message, fullemail, [RECIPIENT])
                    return HttpResponseRedirect('/email/thankyou/')
                except:
                    print("catch")
                    return HttpResponseRedirect('/email/')
        else:
            print("invalid form")
            return HttpResponseRedirect('/email/')
    else:
        print("pos 2")
        return HttpResponseRedirect('/email/')  
