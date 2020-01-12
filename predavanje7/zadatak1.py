# Napišite program u kojem je zadan rječnik rj = {1:'a',2:'b',3:'c'} i koji zatim stvori novi rječnik u kojem su ključevi iz zadanog rječnika vrijednost u novm rječniku,
# a vrijednost iz zadanog rjčnika ključevi u novom rječniku. Ispišite sadržaj novog riječnika.

rj = {1:'a', 2:'b', 3:'c'}
rj2 = {}
for i in rj.items():
    rj2.update({i[1]:i[0]})
print(rj2)