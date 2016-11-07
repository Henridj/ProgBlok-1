import csv

with open('7_4csv.csv', 'r') as file:
    mostExpensive = None
    leastStocked = None
    totalStock = 0
    highestPrice = 0
    lowestStock = 999999
    reader = csv.DictReader(file, delimiter = ';')

    for row in reader:
        price = float(row['Prijs'])
        stock = int(row['Voorraad'])
        totalStock += stock
        if price > highestPrice:
            highestPrice = price
            mostExpensive = row
        if stock < lowestStock:
            lowestStock = stock
            leastStocked = row

    print('Het duurste artikel is', mostExpensive['Naam'], 'en die kost', mostExpensive['Prijs'], 'Euro')
    print('Er zijn slechts', leastStocked['Voorraad'], 'exemplaren in voorraad van het product met nummer', leastStocked['Artikelnummer'])
    print('In totaal hebben wij', totalStock, 'producten in ons magazijn liggen')

print()
