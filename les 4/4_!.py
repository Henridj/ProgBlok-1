#4_1

def convert(temp):
    fahrTemp = temp * 1.8 + 32
    return fahrTemp

def table():
    print('{:9} {:9}'.format('   F', 'C'))
    for i in range(-30, 41, 10):
        print("{:6} {:6.1f}".format(convert(i), i))
table()
print()
