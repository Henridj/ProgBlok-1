import time

stations = ['placeholder', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'den Bosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginStation = input('Voer uw beginstation in: ')
eindStation = input('Voer uw eindstation in: ')

print()
time.sleep(1)

if beginStation not in stations:
    print('Dit station zit niet in het traject, uw nieuwe beginstation is: ' + stations[1] + ' traject nummer: 1')
    beginStation = stations[1]

if eindStation not in stations or stations.index(eindStation) < stations.index(beginStation):
    print('dit station zit niet in het traject, uw nieuwe eindstation is: ' + stations[-1] + ' traject nummer: 15')
    eindStation = stations[-1]

beginIndex = stations.index(beginStation)
eindIndex = stations.index(eindStation)
aantStations = eindIndex - beginIndex - 1
prijs = aantStations * 5

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
