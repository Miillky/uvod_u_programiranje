pol='3x^3+x^2+2x+2'
pol_l = pol.split("+")
koef=[]
for i in pol_l:
    if "x" in i:
        pozicija=i.index("x")
    else:
        pozicija=-1
    if pozicija > 0:
        koef.append(i[:pozicija])
    elif pozicija==0:
        koef.append('1')
    elif pozicija==-1:
        koef.append(i)
koef.reverse()
print(koef)

pol='3x^3+x^2+2x+4'
pol_l=pol.split("+")
koef={}
kljuc=len(pol_l)-1
for i in pol_l:
    if "x" in i:
        pozicija=i.index("x")
    else:
        pozicija=-1
    if pozicija > 0:
        koef.update({kljuc:i[:pozicija]})
    elif pozicija==0:
        koef.update({kljuc:'1'})
    elif pozicija==-1:
        koef.update({kljuc:i[0]})
    kljuc-=1
print(koef)

pol="x^9-2x^5-x^3+1"
pol=pol.replace('-','+')
pol_l=pol.split("+")
koef={}
kljuc=len(pol_l)-1
for i in pol_l:
    if "x" in i:
        pozicija=i.index("x")
    else:
        pozicija=-1
    if pozicija > 0:
        koef.update({kljuc:i[:pozicija]})
    elif pozicija==0:
        koef.update({kljuc:'1'})
    elif pozicija==-1:
        koef.update({kljuc:i[0]})
    kljuc-=1
print(koef)

import random
skup1=set()
skup2=set()
for i in range(25):
    skup1.add(random.randint(1,40))
for i in range(15):
    skup2.add(random.randint(1,50))

print('Zajednički brojevi:',skup1.intersection(skup2))
print('Brojevi po kojima se skup1 razlikuje od skupa2:',skup1-skup2)
print('Brojevi po kojima se skup2 razlikuje od skupa1:',skup2-skup1)
print('Broj članova u skupu1: {0} dok je u skupu2: {1}'.format(len(skup1),len(skup2)))
print('Broj članova u uniji skupova je:',len(skup1.union(skup2)))

n = int(input('Unesi broj kućnih ljubimaca:'))
imenik={}
for i in range(n):
    ime = str(input('Unesite ime ljubimca:'))
    if ime == "":
        break
    vrsta = str(input('Unesite vrstu ljubimca:'))
    if vrsta == "":
        break
    imenik.update({ime:vrsta})
ime = str(input('Unesite ime ljubimca za kojeg želite saznati vrstu:'))
print('{0} je {1}'.format(ime,imenik[ime]))

while True:
    n=int(input('Unesite stupanj polinoma(minimalno 1): '))
    if n<1:
        print("Sutpanj mora biti 1 ili veći")
    else:
        break
polinom=""
for i in range(n+1):
    koef = int(input('Unesite koeficijent {0}. stupnja: '.format(i)))
    if koef!=0:
        if koef>=0:
            koef="+"+str(koef)
        else:
            koef="-"+str(abs(koef))
        if i==0:
            polinom=koef+polinom
        else:
            polinom=koef+"x^"+str(i)+polinom
if polinom[1]=="+":
    polinom=polinom[3:]
else:
    polinom=polinom[1:]
print(polinom)