groen = set(['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'])
rood = set(['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'])

print('Overeenkomst: ', groen.intersection(rood))
print('Rood verschil groen: ', rood.difference(groen))
print('Alle stations zonder dubbele: ', groen.union(rood))
