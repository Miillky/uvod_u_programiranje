ocjene = {'nedovoljan':1, 'dovoljan':2, 'dobar':3, 'vrlo dobar':4, 'odlican':5}
print(ocjene)

ParnoNeparno = {'parni': [2,4,6,7,], 'neparni': [1,3,5,7]}
print(ParnoNeparno['parni'])
print(ParnoNeparno['neparni'])

pretvorba = {2:'a', 3:'b', 4:'c'}
print(pretvorba[2])
print(pretvorba[4])

dani = {'1':'pon', '2':'uto', '3':'čet'}
print(dani)

dani['3'] = 'sri'
print(dani)

dani['4'] = 'čet'
print(dani)

for ocjena in ocjene:
    print(ocjena)