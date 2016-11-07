from random import randint

def throw():
    while True:
        aantDubbel = 0
        diceOne = (randint(0,7))
        diceTwo = (randint(0,7))
        add = diceOne + diceTwo
        if diceOne == diceTwo:
            print('----------')
            print(diceOne, '+', diceTwo, '=', add, '(dubbel)')
            aantDubbel += 1
            while True:
                diceOne = (randint(0,7))
                diceTwo = (randint(0,7))
                if diceOne == diceTwo:
                    aantDubbel += 1
                    print(diceOne, '+', diceTwo, '=', add, '(dubbel)')
                    if aantDubbel == 3:
                        print('gevangenis')
                        print('----------')
                        break
                else:
                    print('----------')
                    print(diceOne, '+', diceTwo, '=', add)
                    break

        else:
            print(diceOne, '+', diceTwo, '=', add)

throw()
