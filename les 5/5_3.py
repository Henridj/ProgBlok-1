invoer = '5-9-7-1-7-8-3-2-4-8-7-9'

lijstInvoer = invoer.split('-')
lijstInvoer.sort()
print(lijstInvoer)

lijstMax = max(lijstInvoer)
print('Het grootste getal is:', lijstMax)

lijstMin = min(lijstInvoer)
print('Het kleinste getal is:', lijstMin)

lijstLen = len(lijstInvoer)
print('Aantal getallen:', lijstLen)

print(type(lijstInvoer))

print(sum(lijstInvoer[0:12]))
