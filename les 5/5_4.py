totaal = []

while True:
    getal = int(input('Geef een getal:', ))
    if getal is not 0:
        totaal.append(getal)
    else:
        print('Er zijn', len(totaal), 'getallen in gevoerd, de som is:', sum(totaal))
        break
