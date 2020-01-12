ocjene = {'nedovoljan':1, 'dovoljan':2, 'dobar':3, 'vrlo dobar':4, 'odlican':5}

print(len(ocjene))

print(ocjene['dobar'])

del(ocjene['nedovoljan'])

print('dobar' in ocjene)

print('nedovoljan' in ocjene)