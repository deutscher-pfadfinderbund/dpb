# Generated by Django 2.2.1 on 2019-05-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('intern', '0037_auto_20190525_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
        migrations.AlterField(
            model_name='state',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
    ]
