#1_4
cijferIcor = 7
cijferProg = 6
cijferCsn = 6
gemiddelde = (cijferIcor + cijferProg + cijferCsn)/3
print(gemiddelde)

cijferPunt = 30
beloning = (cijferPunt * cijferIcor) + (cijferPunt * cijferProg) + (cijferPunt * cijferCsn)
print(beloning)

overzicht = 'Mijn gemiddelde is een: ' + str(gemiddelde) + ' levert: ' + str(beloning) +' op'
print(overzicht)
