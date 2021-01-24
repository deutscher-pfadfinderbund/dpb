from django.core.validators import RegexValidator
from django.db import models


class Person(models.Model):
    salutation = models.CharField("Anrede", max_length=50)
    title = models.CharField("Titel", max_length=50, null=True)
    first_name = models.CharField('Vorname', max_length=50)
    last_name = models.CharField('Nachname', max_length=50)
    nickname = models.CharField('Fahrtenname', max_length=50, null=True)
    birthdate = models.DateField("Geburtstag", null=True)
    date_of_death = models.DateField("Todestag", null=True)
    email = models.EmailField("Email", null=True)

    notes = models.TextField("Anmerkung", null=True, blank=True)

    def common_name(self):
        return f"{self.first_name} {self.last_name}"

    def postal_name(self):
        return f"{self.salutation} {self.first_name} {self.last_name}"

    def __str__(self):
        if self.nickname:
            return f"{self.first_name} '{self.nickname}' {self.last_name}"
        else:
            return self.common_name()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Personen'


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField("Straßenname", max_length=100)
    zip = models.CharField("PLZ", max_length=10)
    town = models.CharField("Stadt", max_length=50)


class PhoneNumber(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    label = models.CharField("Bezeichner", max_length=100)
    phone_regex = RegexValidator(regex=r'^\d+$')
    number = models.CharField(validators=[phone_regex], max_length=20)


class Group(models.Model):
    name = models.CharField("Bezeichner")
    part_of = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
