# -*- coding: utf-8 -*-

from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Home(models.Model):
    # Disponibilities
    dispo_from = models.DateField(verbose_name=u"Disponible à partir du", null=True)
    dispo_to = models.DateField(verbose_name=u"Disponible jusqu'au", null=True, blank=True)
    status = models.TextField(verbose_name=u"Statut (telephone ou non...)")

    # Last time user was contacted
    last_contact = models.DateTimeField(verbose_name=u"Dernier contact", null=True, blank=True)

    # Available places
    places = models.IntegerField(verbose_name=u"Places diponibles")
    services = models.TextField(verbose_name="Services d'accueil proposés en plus d'un lit")

    # Coordinates
    address = models.TextField(verbose_name=u"Adresse")
    phone = models.CharField(max_length=50, verbose_name=u"Numéro de téléphone")
    email = models.EmailField(verbose_name=u"Adresse email")
    name = models.CharField(max_length=200, verbose_name=u"Nom")

    # Languages
    languages = models.TextField(verbose_name=u"Langues parlées")

    user_prefs = models.TextField(verbose_name=u"Conditions d'accueil", null=True, blank=True)
    remarks = models.TextField(verbose_name=u"Remarques", null=True, blank=True)

    tags = TaggableManager()
