#3_5

grondGetal = [1,-2,3,4,-5,6,-7,8,9]

def kwad_som(grondGetal):
    totaal = 0
    for i in grondGetal:
        if i > 0:
            totaal = totaal + i**2
    return totaal

print(kwad_som(grondGetal))
