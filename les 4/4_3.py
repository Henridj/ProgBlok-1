#4_3
print()

testFile = open('test.txt', 'r')
regels = testFile.readlines()
print('deze file telt ' + str(len(regels)) + ' regels')
kaartnummers = []
for regel in regels:
    nummer, naam = regel.split(', ')
    kaartnummers.append(int(nummer))
print('het grootste kaartnummer is: ' + str(max(kaartnummers)) +
       ' en dat staat op regel ' + str(kaartnummers.index(max(kaartnummers)) +1))
testFile.close()
