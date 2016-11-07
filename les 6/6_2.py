
def getTicker(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    tickers = {}
    for i in lines:
        t = i.replace('\n', '').split(':') # remove line break
        tickers[t[0]] = t[1]

    return tickers

tickers = getTicker('6_2.txt')
print(tickers)

while True:
    name = input('Naam van het bedrijf:')

    if name in tickers:
        print('Ticker symbool: ', tickers[name])
        break
    else:
        print('Bedrijf niet gevonden.')

    print()

while True:
    isBedrijf = False
    naamBedrijf = None
    name = input('Ticker van de naam: ')

    for i in tickers:
        if tickers[i] == name:
            isBedrijf = True
            naamBedrijf = i

    if isBedrijf = True:
        print('Naam van het bedrijf:', naamBedrijf)
        break
    else:
        print('Ticker niet gevonden.')


# while True:
#     name = input('Ticker van de naam: ')
#
#     if name in tickers.values():
#         print('Bedrijf naam: ', )
#         break
#     else:
#         print('Ticker niet gevonden.')
#
#     print()
