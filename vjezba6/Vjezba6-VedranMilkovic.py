from math import pow

N = int(input("unesite prirodan broj N: "))
zbroj = 0
if N <= 0:
    print("broj nije prirodan")
else:
    for i in range(1, N + 1):
        zbroj+= pow(i*2, 2)

print("zbroj kvardrana prvih {0} parnih prirodnih brojeva je {1}".format(N, zbroj))

from time import sleep

minute = int(input("unesite broj minuta: "))
sekunde = int(input("unesite broj sekundi: "))
if minute <= 0 and sekunde <= 0:
    print("minute i sekeunde moraju biti realni brojevi")
else:
    for minuta in range(minute, -1, -1):
        for sekunda in range(sekunde, -1, -1):
            print(f"{minuta} minuta, {sekunda} sekunda")
            sleep(1)
        sekunde=59


n = int(input("unesite prirodan broj N: "))
umnozak = 1
if n < 0 or n%1 != 0:
    print("Greška - uneseni broj nije prirodan")
else:
    i = 1
    while i < n+1:
        umnozak *=(i*2-1)
        i+=1
print("umnožak prvih {0} neparnih prirodnih brojeva je {1}".format(n,umnozak))

n=int(input("Unesite prirodan broj N:"))
i=1
ispravno=True
minim=1000000
maxim=-1000000

if n<0 or n%1!=0:
    print("Greška - uneseni broj nije prirodan")
else:
    while i<=n:
        br=float(input("Unesite realan broj:"))
        if br>1000000 or br<-1000000:
            print("Uneseni broj mora biti unutar raspona -1000000 do 1000000")
            ispravno=False
            break
        if br>maxim:
            maxim=br
        if br<minim:
            minim=br
        i+=1
        if ispravno:
            print('Najmanji broj je:',minim)
            print('Najveći broj je:',maxim)

ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")

print( "{0}, {1}".format( ime.capitalize(), prezime.capitalize() ) )

string = str( input("unesite proizvodljni string: ") )
for i in string:
    print(i+"-", end="")

brojImena = int(input("unesite broj imena N: "))
muskaImena = 0
zenskaImena = 0
while brojImena > 0:
    ime = str(input("unesite ime: "))
    print(ime[-1])
    if ime[-1] == "a":
        muskaImena +=1
    else:
        zenskaImena +=1
    brojImena -= 1

print("Uneseno je {0} ženskih i {1} muških imena".format(zenskaImena, muskaImena))

string = str( input("unesite proizvoljni string: ") )
noviString = ""
for i in range(0, len(string)-1, 2):
    noviString += string[i]

print(noviString)

tekst = str(input("unesite rijec: "))
okrenuti, rez1, rez2, rez3 = "", "NE", "DA", "NE"
for i in tekst:
    okrenuti = i + okrenuti
if tekst==okrenuti:
    rez1 = "DA"
print("Obrtanje riječi - Riječ je palindrom:",rez1)

j=0
for i in range(len(tekst)):
    j-=1
    if tekst[i]!=tekst[j]:
        rez2 = "NE"
        break
print("Usporedba obrnutih indeksa - Riječ je palindrom:",rez2)

string = str(input("Upisite recenicu: "))
print("Broj rijeci u recenici je: ", string.count(" ")+1 )