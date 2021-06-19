"""
Endlich ein modernes Adressverzeichnis für unseren Bund!
"""
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import render

from adressverzeichnis.models import ManuelleBerechtigung, Person


def index(request: HttpRequest):
    return render(request, "adressverzeichnis/index.html")


def matching_persons(organ_name, **kwargs):
    """
    :param organ_name: The name of the `Organ` to query against.
    :param kwargs: Can be a filter for any attribute of `ManuelleBerechtigung`
    :return: List of all `Persons` that match the desired `ManuelleBerechtigung`
    """
    return [berechtigung.person for berechtigung in
            ManuelleBerechtigung.objects
                .filter(organ__name=organ_name, **kwargs)
                .select_related('person')]


@login_required
def csv_export(request):
    organ = request.GET["organ"]
    types = request.GET["types"]

    if organ and types:
        types = types.lower().split(",")

        kwargs = {}
        if "protokoll" in types:
            kwargs["bekommt_protokoll"] = True

        if "einladung" in types:
            kwargs["bekommt_einladung"] = True

        if "stimmrecht" in types:
            kwargs["hat_stimmrecht"] = True

        persons = matching_persons(organ, **kwargs)

        return Person.export_as_csv(persons)
    else:
        return HttpResponseBadRequest(content="organ and types needs to be set")
