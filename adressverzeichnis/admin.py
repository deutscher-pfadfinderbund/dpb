# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
# speichere zuletzt angefasst von nutzer und wann
import csv

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
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


class AmtListFilter(admin.SimpleListFilter):
    title = "Amt"
    parameter_name = "amt"

    def lookups(self, request, model_admin):
        return [(amt_typ.pk, amt_typ) for amt_typ in AmtTyp.objects.all()]

    def queryset(self, request, queryset: QuerySet):
        if self.value():
            amt_typ_pk = int(self.value())
            return queryset.filter(amt__typ__pk__exact=amt_typ_pk)

        return queryset


class GruppierungTypListFilter(admin.SimpleListFilter):
    title = "Gruppierungstyp"
    parameter_name = "gt"

    def lookups(self, request, model_admin):
        return [(gruppierungs_typ.pk, gruppierungs_typ) for gruppierungs_typ in GruppierungsTyp.objects.all()]

    def queryset(self, request, queryset: QuerySet):
        if self.value():
            grupperierung_typ_pk = int(self.value())
            return queryset.filter(amt__gruppierung__typ__pk__exact=grupperierung_typ_pk)

        return queryset


@admin.register(Person)
class PersonAdmin(ErstelltModifiziertAdmin):

    def aemter(self, person: Person):
        return [f"{amt.typ} - {amt.gruppierung}" for amt in person.amt_set.all()]

    aemter.short_description = "Ämter"

    def export_as_csv(self, request: HttpRequest, queryset):
        field_names = ['id', 'anrede', 'titel', 'vorname', 'nachname', 'fahrtenname', 'geburtstag', 'todestag', 'stand',
                       'email',
                       'anmerkung', 'veraendert', 'nrw', 'nicht_abdrucken']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=anschriftenverzeichnis.csv'
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)
        for person in queryset:
            writer.writerow([getattr(person, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export (csv)"

    list_display = ("__str__", "fahrtenname", "vorname", "nachname", "aemter")
    search_fields = ("fahrtenname", "vorname", "nachname",)
    list_filter = (AmtListFilter, GruppierungTypListFilter, "stand", "nicht_abdrucken")
    actions = ["export_as_csv"]
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


def get_organigram_as_html(gruppierung: Gruppierung):
    untergruppen: QuerySet[Gruppierung] = gruppierung.untergruppen.all()

    if untergruppen:
        untergruppen_html = format_html_join(
            "\n", "<li>{}</li>",
            [[get_organigram_as_html(untergruppe)] for untergruppe in untergruppen],
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
    readonly_fields = ["organigram"]

    def organigram(self, instance: Gruppierung):
        return get_organigram_as_html(instance)

    organigram.short_description = "Organigramm"
