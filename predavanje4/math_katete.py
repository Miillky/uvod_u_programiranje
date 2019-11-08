# Napišite program koji od korisnika taži vrijednosti dviju kateta trokuta (prirode brojeve),
# te na temelju njih ispisuje vrijednost hipotenuze trokuta:
from math import sqrt

a=int(input("Unesite duljinu katete a: "))
b=int(input("Unesite duljinu katete b: "))
print("Duljina hipotenuze trokuta je:", sqrt(a**2 + b**2))