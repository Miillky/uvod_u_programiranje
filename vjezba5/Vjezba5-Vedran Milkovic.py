""" N = int(input('Unesi prirodan broj manji od 100: '))

if N >= 100 and N < 0:
    print('Greška - uneseni broj je manji od 0 ili veći od 99 ili nije prirodan')
else:
    print('# ' * N) """

""" N = int(input('Unesite prirodan broj N: '))
prvihN = int(input('Prikažite prvih N brojeva: '))
parniBrojevi = []
neparniBrojevi = []

for broj in range(0, N+1):
    if broj <= prvihN:
        if broj % 2 == 0:
            parniBrojevi.append(broj)
        elif broj % 2 == 1:
            neparniBrojevi.append(broj)

print('Parni brojevi:\n', " ".join(str(x) for x in parniBrojevi))
print('Neparni brojevi:\n', " ".join(str(x) for x in neparniBrojevi)) """

""" N = int(input('Unesite priodan broj: '))
for broj in range(N, 1, -1):
    print(broj, '-', broj**2) """

""" N = int(input('Unesite priodan broj: '))
faktorijela = 1
for broj in (range(1, N+1)):
    faktorijela = broj * faktorijela

print(faktorijela) """

""" brojStudenata = int(input('Unesite broj studenata u razredu: '))
ukupnaVisina = 0
i = 1
while i <= brojStudenata:
   ukupnaVisina += int(input('Unesite visinu {0}. studenta: '.format(i) ) )
   i += 1

prosjecnaVisina = ukupnaVisina / brojStudenata
print('Prosječna visina studenata je: ', prosjecnaVisina) """

""" N = int(input("Unesite prirodan broj N: "))
suma=0
i=0
while i <= N:
    if i % 2 == 1:
        suma+= i
    i += 1

print('Suma svih neparnih brojeva do {0} je:'.format(N), suma )
 """

""" import math
x = int(input('Unesite x: '))
y = int(input('Unesite y: '))

while True:
    x = int(input('Unesite x: '))
    y = int(input('Unesite y: '))
    if x + y < 0:
        print('Zbroj parametara ne smije biti manji od 0')
        continue
    break

z = math.sqrt(x+y)/math.sin(x+y)
print("Z je jednak:", z)
 """

""" import math
x = int(input('Unesite x: '))
y = int(input('Unesite y: '))

while True:
    x = int(input('Unesite x: '))
    y = int(input('Unesite y: '))
    if  x < 0:
        print('Parametar x ne smije biti manji od 0')
        continue
    break

z = math.sin(x**y)*math.sqrt(x)/(x*y)
print("Z je jednak:", z) """

""" x = int(input("Unesite x: "))
y = int(input('Unesite y: '))

if x < 0 or x%1 != 0 or y < 0 or y%1 != 0:
    print("Greška - uneseni broj nije prirodan")
else:
    if x<y:
        pomocna=x
    else:
        pomocna=x
    while pomocna > 0:
        if x%pomocna==0 and y%pomocna==0:
            print("Najveći zajednički djelitelj je broj:", pomocna)
            break
        pomocna-=1 """