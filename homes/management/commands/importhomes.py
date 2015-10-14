from pyexcel_ods import get_data
import json
import csv

from django.core.management.base import BaseCommand, CommandError
from homes.models import Home

FILE_NAME1 = "data/dispatching famille AEAD.ods"

class Command(BaseCommand):
    def handle1(self, data):
        data = data["Listing complet nouveau"]
        for i in range(11, 309):
            # 2 : Premier jour de dispo
            # 3 : heure dispo
            # 9 : nombre de jours
            row = data[i]
            home = Home()
            home.last_contact = row[0] if row[0] else None
            home.name = row[4]
            try:
                phone = int(row[5])
                home.phone = "0" + str(phone)
            except:
                if row[5]:
                    home.phone = str(row[5]) if row[5][0] == "0" else "0" + row[5]
                else:
                    home.phone = ""
            home.user_prefs = unicode(row[10]) + '\n' + unicode(row[11])
            home.places = 0
            home.languages = row[13]
            
            status = ""
            if row[20] == "D":
                status = "A deja des refugies"
            elif row[20] == "M":
                status = "A appeler absolument ce mercredi"
            elif row[20] == "J":
                status = "Dispo avant jeudi"
            elif row[20] == "K":
                status = "Pas dispo avant jeudi"
            elif row[20] == "T":
                status = "On a pas telephone"
            elif row[20] == "C":
                status = "Il faut les rappeler SEJOUR COURT"
            elif row[20] == "L":
                status = "Il faut les rappeler SEJOUR LONG"
            home.remarks = unicode(row[19]) + '\n' + status
            home.save()

    def handle(self, *args, **options):
        self.handle1(get_data(FILE_NAME1))