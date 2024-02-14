with open('sneakers.csv') as forrasfajl:
    forrasfajl.readline()

    for sor in forrasfajl:
        cip = []
        valami = sor.strip().split(',')
        cip.append(valami)
        cipok = []
        x = 0
        for x in range(len(cip)):
            cipo = {'title': cip[x][0],
                    'color': cip[x][1],
                    'full_price': cip[x][2],
                    'price': cip[x][3],
                    'publish_date': cip[x][4]}
            print(f'{cipo['color'],cipo['title']}')

            x = x + 1
