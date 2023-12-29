# Generated by Django 3.2.20 on 2023-12-29 21:08

from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    Item = apps.get_model('archive', 'Item')
    DocType = apps.get_model('archive', 'DocType')

    existing_doctypes = (
        "Adressverzeichnis",
        "Chronik / Dokumentation",
        "Fahrtenbericht",
        "Kalender",
        "Lagerheft",
        "Lebensbericht",
        "Liederbuch",
        "Ordnung",
        "Protokoll",
        "Reden",
        "Schöpferisches (Gedicht, Lieder, ...)",
        "Schriftwechsel",
        "Sonstiges",
        "Zeitschrift",
        "Zeitungsartikel",
    )

    DocType.objects.bulk_create([DocType(name=existing_doctype) for existing_doctype in existing_doctypes])


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_doctype'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='document_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.doctype'),
        ),
        migrations.RunPython(code=forwards_func, atomic=True)
    ]
