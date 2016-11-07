while True:
    woordVier = input('Geef een 4 letter woord: ')
    if len(woordVier) is not 4:
        print(woordVier, 'heeft', len(woordVier), 'letters.')
    else:
        print(woordVier, 'heeft inderdaad', len(woordVier), 'letters.')
        break
