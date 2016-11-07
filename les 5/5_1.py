maand = int(input('maandnummer: '))

def seizoen(maand):
    if maand >= 3 and maand <= 5:
        return('lente')
    elif maand >= 9 and maand <= 11:
        return('herfst')
    return maand

print(seizoen(maand))
