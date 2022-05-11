# Generated by Django 4.0.4 on 2022-05-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
                ('date_parution', models.DateField(blank=True, null=True)),
                ('nombre_pages', models.IntegerField()),
                ('resume', models.TextField(blank=True, max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=15)),
            ],
        ),
    ]
