tekst=str(input("Unesite string: "))
lista1 = list(tekst)
print("Pretvorba stringa u listu - list: ",lista1)
lista2 = tekst.split(' ')
print("Pretvorba stringa u listu - split: ",lista2)

tekst = input("Unesi tekst: ")
brojac, slova = 0, ""
for i in tekst:
    if i.isdigit():
        brojac+=1
    if 96 < ord(i) < 123:
        slova+=i
print("Mala slova u stringu: ", slova)
print("Broj znamenaka u stringu: ", brojac)

while True:
    n = int(input("Unesite broj elemenata liste: "))
    if n<1:
        print("Unesite pozitivan cijeli broj!")
        continue
    break
lista = []
for i in range(n):
    element=input("Unesite {0}. element liste: ".format(i))
    lista.append(element)
lista.reverse()
print("Elementi liste su: ", end="")
for i in lista:
    print(i, end=" ")
tekst="".join(lista)
print("\nString je:", tekst)

tekst = input("Unesi tekst: ")
rijec=""
for i in tekst:
    if i != " ":
        rijec+=i
    elif len(rijec)>0:
        print(rijec)
        rijec = ""
print(rijec)

string=input("Unesite niz elemenata odvojenih razmakom: ")
elementi=string.split(' ')
elementi.reverse()
for i in elementi:
    print(i, end=' ')

import math
x1=int(input("Unesite x koordinatu prve točke: "))
y1=int(input("Unesite y koordinate prve točke: "))
x2=int(input("Unesite x koordinate druge točke: "))
y2=int(input("Unesite y koordinate druge točke: "))

t1=(x1,y1)
t2=(x2,y2)
lista = [t1,t2]

h1=math.sqrt(abs(lista[0][0])**2 + abs(lista[0][1]**2))
h2=math.sqrt(abs(lista[1][0])**2 + abs(lista[1][1]**2))

if h1 < h2:
    print("Ishodištu je bliža toča x:{0}, y:{1}".format(lista[0][0], lista[0][1]))
elif h2 < h1:
    print("Ishodištu je bliža toča x:{0}, y:{1}".format(lista[1][0], lista[1][1]))