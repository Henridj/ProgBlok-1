#2_3 / 2_4

leeftijd = int(input('Je leeftijd: '))
paspoort = input('Heb je en Nederlands paspoort ja/nee? ')

if leeftijd > 17 and paspoort == 'ja':
    print('congratz, je mag stemmen')
else:
    print('Sorry, je mag niet stemmen')
