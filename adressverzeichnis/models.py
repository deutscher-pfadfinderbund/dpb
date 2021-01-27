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
    strasse = models.TextField("Straßenname")
    zusatz = models.TextField("Zusatz")
    plz = models.TextField("PLZ")
    stadt = models.TextField("Stadt")


class Telefon(ErstelltModifiziertModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    label = models.TextField("Bezeichner")
    phone_regex = RegexValidator(regex=r'^\d+$')
    nummer = models.TextField("Nummer", validators=[phone_regex])


class Gruppierung(ErstelltModifiziertModel):
    name = models.TextField("Bezeichner")
    obergruppe = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)


class Amt(ErstelltModifiziertModel):
    bezeichnung = models.TextField("Bezeichnung")
    gruppierung = models.ForeignKey(Gruppierung, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
