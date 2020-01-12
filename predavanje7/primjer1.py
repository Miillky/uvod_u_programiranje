# Upis i ispis elemenata rječnika uz pomoć metoda update() te items() - bolji ispis rezultata
n = int(input('Broj elemenata rjecnika: '))
a = {}
for i in range(n):
    kljuc = input('Upisi kljuc: ' )
    vrijednost = input('Upisi vrijednost:' )
    a.update({kljuc:vrijednost})
for k in a.items():
    print('Kljuc: {0}, vrijednost: {1}'.format(k[0],k[1]))