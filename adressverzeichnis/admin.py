# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
# speichere zuletzt angefasst von nutzer und wann

from django.contrib import admin

from .models import Person, Amt, AmtTyp, GruppierungsTyp, Gruppierung, Adresse, Telefon


class ErstelltModifiziertAdmin(admin.ModelAdmin):
    readonly_fields = ("erstellt", "erstellt_von", "veraendert", "veraendert_von")

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()

        for instance in instances:
            if not instance.erstellt_von:
                instance.erstellt_von = request.user

            instance.veraendert_von = request.user
            instance.save()

        formset.save_m2m()

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.erstellt_von = request.user
        obj.veraendert_von = request.user
        super().save_model(request, obj, form, change)


class AdresseInline(admin.StackedInline):
    exclude = ["erstellt_von", "veraendert_von"]
    model = Adresse
    extra = 1


class TelefonInline(admin.TabularInline):
    exclude = ["erstellt_von", "veraendert_von"]
    model = Telefon
    extra = 1


@admin.register(Person)
class PersonAdmin(ErstelltModifiziertAdmin):
    fieldsets = [
        ("Person", {"fields": [
            ("anrede", "titel"),
            ("vorname", "nachname"),
            "fahrtenname",
            ("geburtstag", "todestag"),
            "email",
            "anmerkung"
        ]}),
        ("Meta", {"fields": [
            ("erstellt_von", "erstellt"),
            ("veraendert_von", "veraendert")
        ]}),
    ]
    inlines = (AdresseInline, TelefonInline,)


admin.site.register(Amt, ErstelltModifiziertAdmin)
admin.site.register(AmtTyp, ErstelltModifiziertAdmin)
admin.site.register(Gruppierung, ErstelltModifiziertAdmin)
admin.site.register(GruppierungsTyp, ErstelltModifiziertAdmin)
