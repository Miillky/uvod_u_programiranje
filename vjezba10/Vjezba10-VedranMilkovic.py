def zaokruzi(r):
    from math import floor, ceil
    print('Broj {0} zaokružen na najnižu cjelobrojnu vrijednost iznosi {1}, na najvišu iznosi {2}, dok na najbližu iznosi {3}'.format(r, floor(r), ceil(r), round(r)))

zaokruzi(5.765)


def BMI(m,h):
    index = m/h**2
    if index < 20:
        print('Pothranjenost')
    elif index >= 20 and index < 25:
        print('Idealna težina')
    elif index >= 25 and index < 30:
        print("Prekomjerna tjelesna masa")
    else:
        print("Pretilost")

def main():
    BMI(75,1.82)

main()

popis = [3,9,39,23,1]

def ukloni(n):
    from random import randint
    for i in range(n):
        del popis[randint(0, len(popis)-1)]


import prosti_brojevi

prosti_brojevi.prost_raspon(4,15)
print(prosti_brojevi.prost_prebroji(3,16))
print(prosti_brojevi.prost_n(7))

import izracun

print(izracun.main())

import loto

loto.main()