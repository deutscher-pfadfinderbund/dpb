from django.db import migrations

def forwards_func(apps, _schema_editor):
    Item = apps.get_model('archive', 'Item')
    DocType = apps.get_model('archive', 'DocType')

    for item in Item.objects.all():
        doctype = item.doctype
        if not doctype:
            continue
        if doctype == "Chronik/Dokumentation":
            doctype = "Chronik / Dokumentation"
        item.document_type = DocType.objects.get(name=doctype)
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_item_document_type'),
    ]

    operations = [
        migrations.RunPython(code=forwards_func, atomic=True)
    ]
