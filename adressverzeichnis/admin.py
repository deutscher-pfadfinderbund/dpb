# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
# speichere zuletzt angefasst von nutzer und wann

from django.contrib import admin

from .models import Person, Amt, GruppierungsTyp, Gruppierung, Adresse, Telefon

admin.site.register(Amt)
admin.site.register(Gruppierung)
admin.site.register(GruppierungsTyp)


class ErstelltModifiziertAdmin(admin.ModelAdmin):
    exclude = ["erstellt_von", "veraendert_von"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.erstellt_von = request.user
        obj.veraendert_von = request.user
        super().save_model(request, obj, form, change)


class AdresseInline(admin.StackedInline):
    model = Adresse
    extra = 1


class TelefonInline(admin.TabularInline):
    model = Telefon
    extra = 1


@admin.register(Person)
class PersonAdmin(ErstelltModifiziertAdmin):
    inlines = (AdresseInline, TelefonInline,)
