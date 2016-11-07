studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemStudent(studentencijfers):
    totLijst = []
    for i in studentencijfers:
        somGem = sum(i) / 3
        totLijst.append(somGem)
    return totLijst

def studentGem(studentencijfers):
    totLijst = []
    for i in studentencijfers:
        totLijst.append(sum(i) / 3)
    totLijst = sum(totLijst) / 4
    totLijst = int(totLijst)
    return totLijst


print(gemStudent(studentencijfers))
print(studentGem(studentencijfers))
