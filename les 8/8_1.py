import xmltodict

xml = xmltodict.parse(open('8_1xml.xml', 'rb'))
artikelen = xml['artikelen']['artikel']

for i in artikelen:
    print('-', i['naam'])
