with open('sneakers.csv') as forrasfajl:
    forrasfajl.readline()
    lista = []
    for sor in forrasfajl:
        valami = sor.strip().split(',')
        lista.append(valami)

print(f'1 - title', '\n', '2 - color', '\n', '3 - full price''\n', '4 - current price', '\n', '5 - publish date')
valasztas = int(input('Add meg a számot'))

x = 0
for x in range(len(lista)):
    szin = ('color:', lista[x][1])
    ar = ('current_price:', lista[x][2])
    teljes_ar = ('full_price:', lista[x][3])
    datum = ('publish_date:', lista[x][4])
    nev = ('title:', lista[x][0])

    if valasztas == 1:
        print(f'{nev}', '\n', szin, '\n', ar, '\n', teljes_ar, '\n', datum)
    elif valasztas == 2:
        print(f'{szin}', '\n', ar, '\n', teljes_ar, '\n', datum, '\n', nev)
    elif valasztas == 3:
        print(f'{teljes_ar}', '\n', datum, '\n', nev, '\n', szin, '\n', ar)
    elif valasztas == 4:
        print(f'{ar}', '\n', teljes_ar, '\n', datum, '\n', nev, '\n', szin)
    else:
        print(f'{nev}', '\n', szin, '\n', ar, '\n', teljes_ar, '\n', datum)

    x = x + 1
