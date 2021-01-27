# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
# speichere zuletzt angefasst von nutzer und wann

from django.contrib import admin

from .models import Person, Amt, GruppierungsTyp, Gruppierung, Adresse, Telefon

admin.site.register(Person)
admin.site.register(Amt)
admin.site.register(Gruppierung)
admin.site.register(Adresse)
admin.site.register(Telefon)
admin.site.register(GruppierungsTyp)
