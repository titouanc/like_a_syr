from pyexcel_ods import get_data
import json
import csv

from django.core.management.base import BaseCommand, CommandError
from homes.models import Home

FILE_NAME = "data/dispatching famille AEAD.ods"

class Command(BaseCommand):
    def handle1(self, data):
        data = data["Listing complet nouveau"]
        for i in range(11, 309):
            row = data[i]
            home = Home()
            home.last_contact = row[0] if row[0] else None
            home.remarks = unicode(row[1]) + "/"
            home.name = row[4]
            home.phone = row[5]
            home.user_prefs = unicode(row[10]) + "/"
            home.user_prefs += unicode(row[11]) + "/"
            home.languages = row[13]
            if row[20] == "D":
                home.status = "A deja des refugies"
            elif row[20] == "M":
                home.status = "A appeler absolument ce mercredi"
            elif row[20] == "J":
                home.status = "Dispo avant jeudi"
            elif row[20] == "K":
                home.status = "Pas dispo avant jeudi"
            elif row[20] == "T":
                home.status = "On a pas telephone"
            elif row[20] == "C":
                home.status = "Il faut les rappeler SEJOUR COURT"
            elif row[20] == "L":
                home.status = "Il faut les rappeler SEJOUR LONG"
            home.save()

    def handle(self, *args, **options):
        data = get_data(FILE_NAME)
        self.handle1(data)