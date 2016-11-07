gebruiker = input('Uw naam: ')
beginStation = input('Uw begin station: ')
eindStation = input('Uw eind station: ')

toEncode = (gebruiker + ' ' + beginStation + ' ' + eindStation)
print(toEncode)

def encode(toEncode):
    for i in toEncode:
        ASCII = ord(i) + 3
        tekens = chr(ASCII)
        print(tekens, end = '')

encode(toEncode)


#           geordend    muteerbaar  iterable    dubbele waarden toegestaan
#   tuple      ja          nee         ja          ja
#   dictionary nee         ja          nee         nee
#   set        nee         ja          nee         nee
#   list       ja          ja          ja          ja
