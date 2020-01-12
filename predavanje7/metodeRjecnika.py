ocjene = {'nedovoljan':1, 'dovoljan':2, 'dobar':3, 'vrlo dobar':4, 'odlican':5}

# keys()
print(ocjene.keys())

# values()
print(ocjene.values())

# items()
print(ocjene.items())

# update()
ocjene.update({'fenomenalan':6})
print(ocjene)

# get()
print(ocjene.get('nedovoljan'))

print(ocjene.get('nedovoljannn'))

print(ocjene.get('nedovoljannn', -1))

print(ocjene.get('nedovoljan', -1))