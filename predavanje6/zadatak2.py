# Napišite program koji od korisnika prima broj N, a zatim uzima N riječi koje sprema u listu. Na kraju ispisuje sadržaj lite
n = int(input("Unesite broj n: "))
L1 = []
for i in range(n):
    tekst = str(input('unesite riječ koju želite dodati u listu: '))
    L1.append(tekst)
print(L1)