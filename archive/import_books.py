import csv

from archive.models import Item


def csv_to_data():
    with open("books.csv", 'r') as file:
        reader = csv.DictReader(file, delimiter=";")
        return [r for r in reader]


def row_to_archive_model(row: dict):
    print("Inspecting {}".format(row.get("Titel")))
    Item(
        signature=row.get("Signatur"),
        author=row.get("Autor", None),
        title=row.get("Titel").strip() if row.get("Titel") else None,
        date=row.get("Datum (Vorlage)").strip(),
        year=int(row.get("Jahr")) if row.get("Jahr") else None,
        place=row.get("OrtVeröffentlichung").strip(),
        doctype=row.get("Dokumenttyp").strip(),
        medartanalog=row.get("Medienart").strip(),
        keywords=row.get("Schlagworte").strip(),
        location=row.get("Standort (analoges Archiv)").strip(),
        source=row.get("Quelle").strip(),
        notes=row.get("Anmerkungen").strip(),
    ).save()


def save_all_rows():
    data = csv_to_data()
    for item in data:
        row_to_archive_model(item)
