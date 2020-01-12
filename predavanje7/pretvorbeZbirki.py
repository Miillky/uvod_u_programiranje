mojset = {0,2,3,4,5,7,8,9,10}
lista = list(mojset)
print(lista)

ntorka = tuple(mojset)
print(ntorka)

# rjecnik = dict(mojset) # greška
ntorka=(123,234,567)
set2 = set(ntorka)
print(set2)

lista = [[1,"ponedjeljak"], [2,"utorak"]]
rjecnik = dict(lista)
print(rjecnik)

set1 = set(rjecnik)
print(set1)

set2 = set(rjecnik.items())
print(set2)

set3 = set(rjecnik.values())
print(set3)