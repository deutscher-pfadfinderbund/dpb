from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("archive", "0009_alter_item_document_type"),
    ]

    operations = [

        # A collation is a set of rules for comparing characters in a database.
        # The 'alphanumeric' collation defined here uses the ICU provider with
        # German locale settings to ensure that strings are sorted in a way that
        # takes numeric values into account (e.g., "item2" comes before "item10").
        migrations.RunSQL("CREATE COLLATION IF NOT EXISTS alphanumeric (provider = icu, locale = 'de@colNumeric=yes');"),
        migrations.AlterField(
            model_name="item",
            name="signature",
            field=models.CharField(
                blank=True,
                db_collation="alphanumeric",
                max_length=50,
                verbose_name="Signatur",
            ),
        ),
    ]