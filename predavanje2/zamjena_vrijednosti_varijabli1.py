# Napišite program koji unosi dva cijela broja te ih sprema u varijable x i y.
# Program nakon toga zamjenjuje vrijednosti varijabli te sadržaj varijabli (x, y) ispisuje na ekran.

x=int(input('Unesi broj x:'))
y=int(input('Unesi broj y:'))
c=x
x=y
y=c
print('Uneseni x je', x, 'dok je uneseni y', y)