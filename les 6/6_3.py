def askNames():
    names = {}
    while True:
        name = input('Enter name: ').capitalize()
        if name == '':
            break

        if name in names:
            names[name] += 1
        else:
            names[name] = 1

    return names

def printNames(names):
    for key, value in names.items():
        if value > 1:
            print('Er zijn', value, 'studenten met de naam:', key)
        else:
            print('Er is', value, 'student met de naam:', key)

names = askNames()
printNames(names)
