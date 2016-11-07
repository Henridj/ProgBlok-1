#4_2

testFile = open('test.txt', 'r')
for line in testFile:
    lijst = line.split(', ')
    naam = lijst[1].replace('\n', '')
    naam2 = lijst[1][:-1]
    nummer = lijst[0]
    print(naam2 + ' heeft kaartnummer: ' + naam)

testFile.close()
