# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
# speichere zuletzt angefasst von nutzer und wann

from django.contrib import admin
from django.db.models import QuerySet
from django.utils.html import format_html_join, format_html

from .models import Person, Amt, AmtTyp, GruppierungsTyp, Gruppierung, Adresse, Telefon, Organ, ManuelleBerechtigung


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
    extra = 0


class TelefonInline(admin.TabularInline):
    exclude = ["erstellt_von", "veraendert_von"]
    model = Telefon
    extra = 0


class AmtInline(admin.TabularInline):
    exclude = ["erstellt_von", "veraendert_von"]
    model = Amt
    extra = 0


class ManuelleBerechtigungInline(admin.TabularInline):
    exclude = ["erstellt_von", "veraendert_von"]
    model = ManuelleBerechtigung
    extra = 0


@admin.register(Person)
class PersonAdmin(ErstelltModifiziertAdmin):
    fieldsets = [
        ("Person", {
            "fields": [
                ("anrede", "titel"),
                ("vorname", "nachname"),
                ("fahrtenname", "stand"),
                ("geburtstag", "todestag"),
                "email",
                "anmerkung",
                ("nicht_abdrucken", "nrw")
            ]
        }),
        ("Meta", {
            "fields": [
                ("erstellt_von", "erstellt"),
                ("veraendert_von", "veraendert")
            ]
        }),
    ]
    inlines = (AmtInline, AdresseInline, TelefonInline, ManuelleBerechtigungInline,)


admin.site.register(Amt, ErstelltModifiziertAdmin)
admin.site.register(AmtTyp, ErstelltModifiziertAdmin)
admin.site.register(GruppierungsTyp, ErstelltModifiziertAdmin)
admin.site.register(Organ, ErstelltModifiziertAdmin)
admin.site.register(ManuelleBerechtigung, ErstelltModifiziertAdmin)


def get_untergruppen_as_html(gruppierung: Gruppierung):
    untergruppen: QuerySet[Gruppierung] = gruppierung.untergruppen.all()

    if untergruppen:
        untergruppen_html = format_html_join(
            "\n", "<li>{}</li>",
            [(get_untergruppen_as_html(untergruppe),) for untergruppe in untergruppen],
        )

        return format_html(
            "<details><summary>{}</summary><ul style='margin-left: 8px'>{}</ul></details>",
            gruppierung, untergruppen_html
        )
    else:
        return gruppierung


@admin.register(Gruppierung)
class GrupppierungAdmin(ErstelltModifiziertAdmin):
    exclude = ["erstellt_von", "veraendert_von"]
    readonly_fields = ("organigram",)

    def organigram(self, instance: Gruppierung):
        return get_untergruppen_as_html(instance)

    organigram.short_description = "Organigram"
