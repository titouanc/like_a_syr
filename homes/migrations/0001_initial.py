# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inscription', models.DateTimeField(auto_now_add=True)),
                ('dispo_from', models.DateField(null=True, verbose_name='Disponible \xe0 partir du')),
                ('dispo_to', models.DateField(null=True, verbose_name="Disponible jusqu'au", blank=True)),
                ('last_contact', models.DateTimeField(null=True, verbose_name="Dernier contact avec l'h\xf4te", blank=True)),
                ('places', models.IntegerField(verbose_name='Places diponibles')),
                ('address', models.TextField(verbose_name='Adresse')),
                ('phone', models.CharField(max_length=50, verbose_name='Num\xe9ro de t\xe9l\xe9phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse email')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('languages', models.TextField(null=True, verbose_name='Langues parl\xe9es', blank=True)),
                ('user_prefs', models.TextField(null=True, verbose_name="Conditions d'accueil (Services offerts, animaux, etc...)", blank=True)),
                ('remarks', models.TextField(null=True, verbose_name="Remarques du service d'accueil", blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
    ]
