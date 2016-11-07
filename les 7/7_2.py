import datetime
import csv

while True:
    tijd = datetime.datetime.now()                                                                      #sets 'tijd' to current time
    tijdFormat = tijd.strftime('%a %d %b %Y')

    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
            exit()
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    dict = {}

    with open('7_2csv.csv', 'r') as myCSVFile:
        reader = csv.DictReader(myCSVFile, delimiter=';')
        for row in reader:
            dict = row
            dict['tijd'] = tijdFormat
            dict['voorl'] = voorl
            dict['achternaam'] = naam
            dict['gbdatum'] = gbdatum
            dict['email'] = email
        with open('7_2csv.csv', 'a', newline='') as myCSVFile:
            writer = csv.DictWriter(myCSVFile, delimiter=';', fieldnames=reader.fieldnames)
            writer.writerow(dict)
