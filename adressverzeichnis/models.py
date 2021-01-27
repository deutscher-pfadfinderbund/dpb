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


class Person(ErstelltModifiziertModel):
    anrede = models.CharField("Anrede", max_length=50)
    titel = models.CharField("Titel", max_length=50, null=True)
    vorname = models.CharField('Vorname', max_length=50)
    nachname = models.CharField('Nachname', max_length=50)
    fahrtenname = models.CharField('Fahrtenname', max_length=50, null=True)
    geburtstag = models.DateField("Geburtstag", null=True)
    todestag = models.DateField("Todestag", null=True)
    email = models.EmailField("Email", null=True)

    anmerkung = models.TextField("Anmerkung", null=True, blank=True)

    def common_name(self):
        return f"{self.vorname} {self.nachname}"

    def postal_name(self):
        return f"{self.anrede} {self.vorname} {self.nachname}"

    def __str__(self):
        if self.fahrtenname:
            return f"{self.vorname} '{self.fahrtenname}' {self.nachname}"
        else:
            return self.common_name()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Personen'


class Adresse(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    label = models.CharField("Bezeichner (Privat, ...)", max_length=50)

    strasse = models.CharField("Straßenname", max_length=100)
    zusatz = models.CharField("Zusatz", max_length=50)
    plz = models.CharField("PLZ", max_length=15)
    stadt = models.CharField("Stadt", max_length=100)
    land = models.CharField("Land", max_length=100, default="Deutschland")

    def __str__(self):
        return "%s %s, %s %s %s".format(self.strasse, self.zusatz, self.plz, self.stadt, self.land)

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adressen'


class Telefon(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    label = models.TextField("Bezeichner (Privat, ...)")
    phone_regex = RegexValidator(regex=r'^\d+$')
    nummer = models.TextField("Nummer", validators=[phone_regex])

    def __str__(self):
        return self.nummer

    class Meta:
        verbose_name = 'Telefonnummer'
        verbose_name_plural = 'Telefonnummern'


class Gruppierung(ErstelltModifiziertModel):
    name = models.TextField("Bezeichner")
    type = models.TextField(choices=[("stamm", "Stamm"), ("js", "Jungenschaft")], null=True, blank=True)
    obergruppe = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gruppierung"
        verbose_name_plural = "Gruppierungen"


class Amt(ErstelltModifiziertModel):
    bezeichnung = models.TextField("Bezeichnung")
    gruppierung = models.ForeignKey(Gruppierung, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Amt"
        verbose_name_plural = "Ämter"
