# Generated by Django 3.2.12 on 2022-03-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vorfreude', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foto',
            field=models.ImageField(default=None, upload_to='', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
