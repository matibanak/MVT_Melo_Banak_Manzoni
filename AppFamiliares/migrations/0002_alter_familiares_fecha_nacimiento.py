# Generated by Django 4.0.5 on 2022-07-04 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamiliares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]