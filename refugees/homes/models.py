# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Home(models.Model):
    # Disponibilities
    dispo_from = models.DateField(verbose_name=u"Disponible à partir du")
    dispo_to = models.DateField(verbose_name=u"Disponible jusqu'au")

    # Available places
    places = models.IntegerField(verbose_name=u"Places diponibles")

    # Coordinates
    address = models.TextField(verbose_name=u"Adresse")
    phone = models.TextField(verbose_name=u"Numéro de téléphone")
    email = models.EmailField(verbose_name=u"Adresse email")
    name = models.TextField(verbose_name=u"Nom")

    remarks = models.TextField(verbose_name=u"Remarques")
