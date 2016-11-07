import datetime

#4_4

print('(typ eind om programma te stoppen)')
deelnemers = []

while True:
    hardloper = input('naam: ')
    tijd = datetime.datetime.now()
    tijdFormat = tijd.strftime('%a %d %b %y, %H:%M:%S - ' + hardloper + '\n')
    deelnemers.append(tijdFormat)
    contestants = open('contestants.txt', 'w')
    for i in deelnemers:
        contestants.write(str(i))
    if hardloper == 'eind':
        break
