import time
import csv
from random import randint

def newVault():
    print()
    print('These are the usable vaults:')
    print()
    vaultList = {}
    with open('vaults.csv', 'r') as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=';')
        for row in reader:
            vaultList[int(row[0])] = row[1]
        for key in range(1, 13):
            value = vaultList[key]
            if value == 'vrij':
                print('Vault {:2} : {}'.format(key, value))
        print()
        try:
            vaultNum = int(input('Choose a vault number (enter 0 if you want to stop): '))
            if vaultNum == 0:
                pass
            elif vaultList[int(vaultNum)] != 'vrij':
                print('This vault is already in use')
                input('Press enter to continue')
                newVault()
            elif vaultNum in vaultList:
                vaultList[vaultNum] = randint(1000, 10000)
                print('Your pincode:', vaultList[vaultNum], 'Rember this to reopen or return your vault!')
                with open('vaults.csv', 'w', newline='') as myCSVFile:
                    writer = csv.writer(myCSVFile, delimiter=';')
                    for key, value in vaultList.items():
                        writer.writerow([key, value])
                print()
                input('Press enter to continue')
        except ValueError:
            print('Input must be a number.')
            input('Press enter to continue')
            newVault()
        except KeyError:
            print('This value has no option.')
            input('Press enter to continue')
            newVault()

    print()

def openVault():
    print()
    vaultList = {}
    with open('vaults.csv', 'r') as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=';')
        for row in reader:
            vaultList[int(row[0])] = row[1]
        try:
            nummer = int(input('Number of Vault you would like to open (enter 0 if you want to stop): '))
            if nummer == 0:
                pass
            elif nummer < 0 or nummer > 12:
                print('This value has no option.')
                input('Press enter to continue')
                openVault()
            for key, value in vaultList.items():
                value = vaultList[key]
                if value == 'vrij' and key == nummer:
                    print('This vault cannot be opened because it is not in use.')
                    input('Press enter to continue')
                    openVault()
                elif value != 'vrij' and key == nummer:
                    pinCode = input('Enter your pincode: ')
                    if pinCode == value:
                        print('Vault', nummer, 'has unlocked!')
                        print()
                        input('Press enter to continue')
                    else:
                        print('Not the right pincode.')
                        input('Press enter to continue')
        except ValueError:
            print('Input must be a number.')
            openVault()
    print()

def returnVault():
    print()
    vaultList = {}
    with open('vaults.csv', 'r') as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=';')
        for row in reader:
            vaultList[int(row[0])] = row[1]
        try:
            nummer = int(input('Number of Vault you would like to return (enter 0 if you want to stop): '))
            if nummer == 0:
                pass
            elif nummer < 0 or nummer > 12:
                print('This value has no option.')
                input('Press enter to continue')
                returnVault()
            for key, value in vaultList.items():
                if value == 'vrij' and key == nummer:
                    print('This vault cannot be returned because it is not in use.')
                    input('Press enter to continue')
                    returnVault()
                elif value != 'vrij' and key == nummer:
                    pinCode = input('Enter your pincode: ')
                    if pinCode == value:
                        vaultList[key] = 'vrij'
                        with open('vaults.csv', 'w', newline='') as myCSVFile:
                            writer = csv.writer(myCSVFile, delimiter=';')
                            for key, value in vaultList.items():
                                writer.writerow([key, value])
                            print('Your vault has been returned.')
                            print()
                            input('Press enter to continue')
                    else:
                        print('Not the right pincode.')
                        input('Press enter to continue')
        except ValueError:
            print('Input must be a number.')
            returnVault()
    print()

def toDo():
    print('options:')
    print()
    print(' 1: I\'d like to get a vault.')
    print(' 2: I\'d like to open my vault.')
    print(' 3: I\'d like to return my vault.')
    print(' 4: Stop.')
    print()
    while True:
        try:
            option = int(input('What would you like to do? (number between 1/4): '))
            if option in range(1, 5):
                if option == 1:
                    newVault()
                elif option == 2:
                    openVault()
                elif option == 3:
                    returnVault()
                elif option == 4:
                    print('Have a nice day!')
                    exit()
                break
            else:
                print('This value has no option.')
        except ValueError:
            print('Input must be a number.')
            toDo()

while True:
    toDo()
