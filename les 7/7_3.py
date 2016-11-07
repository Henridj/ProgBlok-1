import csv

lijst = []
with open('7_3csv.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    maxVal = (max(row[2] for row in reader))

with open('7_3csv.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        if maxVal in row:
            naam = row[0]
            datum = row[1]

print(' De hoogste score is: {} op {} behaald door {}.'.format(maxVal, datum, naam))
