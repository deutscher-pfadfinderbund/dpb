# Generated by Django 5.1.1 on 2024-09-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20190525_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
        migrations.AlterField(
            model_name='linkcategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am'),
        ),
    ]
