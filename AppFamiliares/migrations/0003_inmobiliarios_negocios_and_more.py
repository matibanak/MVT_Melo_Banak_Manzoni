# Generated by Django 4.0.5 on 2022-07-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamiliares', '0002_alter_familiares_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmobiliarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=60)),
                ('localidad', models.CharField(max_length=40)),
                ('mt2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Negocios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='familiares',
            name='fecha_nacimiento',
            field=models.CharField(max_length=40),
        ),
    ]