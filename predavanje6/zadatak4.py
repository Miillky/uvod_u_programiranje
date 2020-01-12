# Program koji od korisnika uzima tri vrijednosti za prvi tuple, i dvije vrijednosti za drugi tuple. Zatim ta dva tuple-a pohranjuje u listu.
# Svaki tuple je jedan član liste. Na kraju ispisuje vrijednost prvog tuple-a, drugog tupl-a i liste:
# 1. član prvog tuplea: 2
# 2. član prvog tuplea: 4
# 3. član prvog tuplea: 6
# 1. član prvog tuplea: 3
# 2. član prvog tuplea: 5
# ('2', '4', '6')
# ('3', '5')
# [('2', '4', '6'), ('3', '5')]

tup1 = ()
tup2 = ()
for i in range(3):
    a = str(input("{0}. član prvog tuplea: ".format(i+1)))
    tup1 = tup1 + (a,)
for j in range(2):
    b = str(input("{0}. član drugog tuplea: ".format(j+1)))
    tup2 = tup2 + (b,)
lista = [tup1, tup2]

print(tup1)
print(tup2)
print(lista)