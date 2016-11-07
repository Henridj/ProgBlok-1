afstandKM = int(input('Hoeveel kilometer moet u reizen: '))
leefTijd = int(input('hoe oud ben je: '))
weekendRit = eval(input('Weekendrit? True/False: '))

def standaardtarief(afstandKM):
    if afstandKM < 0:
        totPrijs = 0
    elif afstandKM < 50:
        totPrijs = afstandKM * 0.80
    else:
        aantKM = afstandKM - 50
        totPrijs = 15 + (aantKM * 0.60)
    return totPrijs


def ritPrijs(leefTijd, weekendRit, afstandKM):
    totPrijs = standaardtarief(afstandKM)
    if weekendRit == True:
        if leefTijd < 0:
            totPrijs = 'Fookin time travelers'
        elif leefTijd < 12 or leefTijd >= 65:
            totPrijs *= 0.65
        else:
            totPrijs *= 0.60
    else:
        if leefTijd < 0:
            totPrijs = 'Fookin time travelers'
        elif leefTijd < 12 or leefTijd >= 65:
            totPrijs *= 0.70
    return totPrijs

print('Dit kost:', ritPrijs(leefTijd, weekendRit, afstandKM), 'euro')
