bedrag = 4356

try:
    personen = int(input('Met hoeveel personen ben je? '))
    if personen < 0:
        print('min getallen zijn niet mogelijk')
    else:
        totaal = bedrag / personen
        print(totaal)
except ZeroDivisionError:
    print('Kan niet delen door 0!')
except ValueError:
    print('Er mogen alleen cijfers opgegeven worden!')
except:
    print('Onjuiste invoer!')
