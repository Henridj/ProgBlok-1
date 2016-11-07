#3_6
list = ['a', 'b', 'c']
print(list)
def wijzig(list):
    list.clear()
    list.append('d')
    list.append('e')
    list.append('f')
    return list
print(wijzig(list))
