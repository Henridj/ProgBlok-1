annuleringen = open('annuleringen.txt', 'r')
regels = annuleringen.readlines()
stationsAnnu = []
for i in regels:
    Annu = i.replace('\n', '').split(': ')[1]
    stationsAnnu.append(Annu)
annuleringen.close()

treinRitten = open('treinritten.txt', 'r')
lines = treinRitten.readlines()
treinRitten.close()

newRitten = open('newRitten.txt', 'w')

for i in lines:
    station = i.replace('\n', '').split('- ')[1]
    if station not in stationsAnnu:
        newRitten.write(i)
newRitten.close()
