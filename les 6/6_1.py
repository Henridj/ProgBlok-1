cijfer = {'jan': 9, 'piet': 7, 'henk': 10, 'han': 6, 'klaas': 9.5, 'kees': 4, 'storm': 9, 'ed': 6, 'jos': 8}

for c in cijfer:
    value = cijfer[c]
    if value >= 9:
        print(c, value)

print()

for key, value in cijfer.items():
    if value >= 9:
        print(key, value)
