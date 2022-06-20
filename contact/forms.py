from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255)
    email = forms.EmailField(label="E-Mail")
    subject = forms.CharField(label="Betreff", max_length=255)
    message = forms.CharField(label="Deine Nachricht", widget=forms.Textarea)
    honeypot = forms.CharField(widget = forms.HiddenInput(), required = False)
