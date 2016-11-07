import time

stations = ['placeholder', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'den Bosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginpunt():
    while True:
        beginStation = input('Voer uw beginstation in: ')
        beginStation = beginStation.capitalize()
        if beginStation not in stations:
            print('Dit station zit niet in het traject, voer het opnieuw in')
        elif beginStation == 'Maastricht':
            print('Het laatste station kan niet het eindstation zijn.')
        else:
            break
    return beginStation

def inlezen_eindpunt(beginStation):
    while True:
        eindStation = input('Voer uw eindstation in: ')
        eindStation = eindStation.capitalize()
        if eindStation not in stations or stations.index(eindStation) < stations.index(beginStation):
            print('dit station zit niet in het traject, voer het opnieuw in')
        else:
            break
    return eindStation

def omroep_reis(beginStation, eindStation):

    beginIndex = stations.index(beginStation)
    eindIndex = stations.index(eindStation)
    aantStations = eindIndex - beginIndex - 1
    prijs = aantStations * 5 + 5

    tussenStations = []

    for i in stations:
        if(stations.index(i) > stations.index(beginStation) and stations.index(i) < stations.index(eindStation)):
            tussenStations.append(i)
    print()
    time.sleep(1)
    print('Uw begin station is: ' + beginStation + ', met traject nummer: ' + str(stations.index(beginStation)))
    print('Tussen stations:')
    for i in tussenStations:
        print('  ~' + i)
    print('Aantal tussen stations: ' + str(aantStations))
    print('Uw eind Station is: ' + eindStation + ', met traject nummer: ' + str(stations.index(eindStation)))
    print('Deze rit kost u ' + str(prijs) + ' euro.')

beginStation = inlezen_beginpunt()
eindStation = inlezen_eindpunt(beginStation)
omroep_reis(beginStation, eindStation)
