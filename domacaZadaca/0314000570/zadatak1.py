# Napišite program koji od korisnika unosi tri broja. Zatim ispisuje tekst:“ Kada zbrojimo brojeve <a> i <b> te nakon toga taj zbroj podijelimo s <c>, rezultat je <rez>“.
# Umjesto <a>,<b> i <c> program ispisuje vrijednosti koje je unio korisnik, dok se rezultat <rez> ispisuje s 3 decimale.

a = int(input('Unesite broj a: '))
b = int(input('Unesite broj b: '))
c = int(input('Unesite broj c: '))

rez = (a + b) / c

print('Kada zbrojimo brojeve {0} i {1} te nakon toga taj zbroj podijelimo s {2}, rezultat je {3:0.3f}'.format(a, b, c, rez))