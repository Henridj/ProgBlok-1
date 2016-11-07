import xmltodict

xml = xmltodict.parse(open('info.xml', 'rb'))
stations = xml['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations:')
for type in stations:
    print('{:4} - {}'.format(type['Code'], type['Type']))

print()
print('Dit zijn alle stations met 1 of meer synoniemen:')
for synoniem in stations:
    if synoniem['Synoniemen']:
        print('{:2} - {}'.format(synoniem['Code'], synoniem['Synoniemen']))

print()
print('Dit is de lange naam van elk station:')
for lang in stations:
    print('{:4} - {}'.format(lang['Code'], lang['Namen']['Lang']))
