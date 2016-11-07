#3_4

def newPw(oldPass, newPass):
    if oldPass != newPass and len(newPass) >= 6:
        out = 'true'
    else:
        out = 'false'
    return out

print(newPw('testtest', 'test575786756'))
