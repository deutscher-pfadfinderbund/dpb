# Generated by Django 3.2.4 on 2021-06-19 20:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('archive', '0003_auto_20190525_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Rückmeldung', 'verbose_name_plural': 'Rückmeldungen'},
        ),
    ]
