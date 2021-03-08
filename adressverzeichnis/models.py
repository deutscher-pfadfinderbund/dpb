from collections import OrderedDict

from django.contrib.auth.backends import UserModel
from django.core.validators import RegexValidator
from django.db import models


class ErstelltModifiziertModel(models.Model):
    erstellt = models.DateTimeField("Erstellt am", auto_now_add=True)
    erstellt_von = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE, related_name="+")

    veraendert = models.DateTimeField("Zuletzt verändert", auto_now=True)
    veraendert_von = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE, related_name="+")

    class Meta:
        abstract = True


staende = [
    ("St.-Georgs-Ritter", "St.-Georgs-Ritter"),
    ("Ordensritter", "Ordensritter"),
    ("St.-Georgs-Knappe", "St.-Georgs-Knappe"),
    ("Späher", "Späher"),
    ("Knappe", "Knappe"),
    ("Jungwolf", "Jungwolf"),
    ("Wölfling", "Wölfling"),

    ("Gildenmeisterin", "Gildenmeisterin"),
    ("Pilgerin", "Pilgerin"),
    ("Novizin", "Novizin"),
    ("Gildin", "Gildin"),
    ("Gildenmädchen", "Gildenmädchen"),
    ("Jungpfadfinderin", "Jungpfadfinderin")
]


class Person(ErstelltModifiziertModel):
    anrede = models.CharField("Anrede", max_length=50, blank=True, default="")
    titel = models.CharField("Titel", max_length=50, blank=True, default="")
    vorname = models.CharField('Vorname', max_length=50)
    nachname = models.CharField('Nachname', max_length=50)
    fahrtenname = models.CharField('Fahrtenname', max_length=50, blank=True, default="")
    geburtstag = models.DateField("Geburtstag", null=True, blank=True)
    todestag = models.DateField("Todestag", null=True, blank=True)
    email = models.EmailField("E-Mail", null=True, blank=True, default="")
    stand = models.TextField("Stand", null=True, blank=True, choices=staende)

    anmerkung = models.TextField("Anmerkung", blank=True, default="")

    nicht_abdrucken = models.BooleanField("Nicht im Adressverzeichnis abdrucken?", default=False)
    nrw = models.BooleanField("Kommt aus NRW?", default=False)

    alte_id = models.PositiveIntegerField("Alte ID", unique=True, blank=True, null=True)

    def common_name(self):
        return f"{self.vorname} {self.nachname}"

    def postal_name(self):
        return f"{self.anrede} {self.vorname} {self.nachname}"

    def __str__(self):
        if self.fahrtenname:
            return f"{self.fahrtenname} ({self.vorname} {self.nachname})"
        else:
            return self.common_name()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Personen'

    def csv_dict(self):
        field_names = ['id', 'anrede', 'titel', 'vorname', 'nachname', 'fahrtenname', 'geburtstag', 'todestag', 'stand',
                       'email',
                       'anmerkung', 'veraendert', 'nrw', 'nicht_abdrucken']

        return OrderedDict({key: self.__dict__[key] for key in field_names})

    def legacy_csv_dict(self):
        csv_dict = self.csv_dict()

        csv_dict |= self.adresse_set.first().csv_dict() if self.adresse_set.first() else {}

        for index, telefonnummer in enumerate(self.telefon_set.all()):
            csv_dict |= telefonnummer.csv_dict(index=index + 1)

        return csv_dict


class Adresse(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    label = models.CharField("Bezeichner (Privat, ...)", max_length=50, blank=True, default="",
                             help_text="(Privat, ...)")

    strasse = models.CharField("Straßenname", max_length=100, blank=True, default="")
    zusatz = models.CharField("Zusatz", max_length=50, blank=True, default="")
    plz = models.CharField("PLZ", max_length=15, blank=True, default="")
    stadt = models.CharField("Stadt", max_length=100, blank=True, default="")
    land = models.CharField("Land", max_length=100, default="Deutschland", blank=True)

    def __str__(self):
        return f"({self.label}) {self.strasse} {self.zusatz}, {self.plz} {self.stadt} {self.land}"

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adressen'

    def csv_dict(self, index=""):
        field_mappings = [("strasse", "Straße"),
                          ("zusatz", "Zusatz"),
                          ("plz", "Postleitzahl"),
                          ("stadt", "Ort"),
                          ("land", "Land")]
        return {label + str(index): getattr(self, key) for (key, label) in field_mappings}


class Telefon(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\d+$')
    nummer = models.CharField("Nummer", validators=[phone_regex], max_length=20)
    label = models.CharField("Bezeichner (Privat, ...)", max_length=50, blank=True)

    def __str__(self):
        return f"Nummer von {self.person} ({self.nummer})"

    class Meta:
        verbose_name = 'Telefonnummer'
        verbose_name_plural = 'Telefonnummern'

    def csv_dict(self, index=""):
        field_mappings = [("nummer", "Telefonnummer"),
                          ("label", "Telefonbezeichner")]
        return {label + str(index): getattr(self, key) for (key, label) in field_mappings}


class GruppierungsTyp(ErstelltModifiziertModel):
    name = models.CharField("Name", max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gruppierungs Typ"
        verbose_name_plural = "Gruppierungs Typen"


class Gruppierung(ErstelltModifiziertModel):
    name = models.CharField("Bezeichner", max_length=100)
    typ = models.ForeignKey(GruppierungsTyp, null=True, blank=True, on_delete=models.SET_NULL)
    obergruppe = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="untergruppen")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gruppierung"
        verbose_name_plural = "Gruppierungen"


class AmtTyp(ErstelltModifiziertModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Amt Typ"
        verbose_name_plural = "Amt Typen"


class Amt(ErstelltModifiziertModel):
    typ = models.ForeignKey(AmtTyp, null=True, on_delete=models.SET_NULL)
    gruppierung = models.ForeignKey(Gruppierung, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    bestaetigt = models.BooleanField("Bestätigt?", default=True)

    def __str__(self):
        return f"{self.typ} - {self.gruppierung} - {self.person}"

    class Meta:
        verbose_name = "Amt oder Mitgliedschaften"
        verbose_name_plural = "Ämter und Mitgliedschaften"


class Organ(ErstelltModifiziertModel):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organ"
        verbose_name_plural = "Organe"


class ManuelleBerechtigung(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)
    bekommt_einladung = models.BooleanField("Bekommt Einladung?", default=False, help_text="Zum überschreiben")
    bekommt_protokoll = models.BooleanField("Bekommt Protokoll?", default=False)

    def __str__(self):
        return f"{self.person} ist teil von {self.organ}"

    class Meta:
        verbose_name = "Manuelle Berechtigung"
        verbose_name_plural = "Manuelle Berechtigungen"
