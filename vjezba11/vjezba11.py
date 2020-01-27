file = open('vjezba11/Programiranje.txt', 'w')
file.write('Danas je jako lijep dan za programiranje!')
file.close()

file = open('vjezba11/brojevi.txt', 'w')
for i in range(100):
    file.write(str(i)+'\n')
file.close()

file = open('vjezba11/ulazno_silazno.txt', 'w')
for i in range(0,100):
    file.write("Ulazno: {0}, silazno: {1} \n".format(i, 100-i))
file.close()

file = open('vjezba11/redak.txt', 'r+')
rows = 0
for i in file:
    print(i)
    rows += 1

if rows <= 3:
    file.write('\nCetvrti redak\nPeti redak')
file.close()

file = open('vjezba11/redak.txt', 'r')
file.readline()
file.readline()
file.readline()
file.seek(file.tell()+3)
print(file.readline())
file.close()

file = open('vjezba11/citanje_brojeva.txt', 'r')
for i in file:
    print(int(i) + 100)
file.close()

file = open('vjezba11/ispis_brojeva.txt')
brojevi = file.readlines()[0].split(' ')
for i in brojevi:
    print(i)
file.close()

ulaz = open('vjezba11/min_max_broj_ulaz.txt', 'r')
izlaz = open('vjezba11/min_max_broj_izlaz.txt', 'w')

for row in ulaz.readlines():
    lista = row.split(' ')
    minBroj = min(lista)
    maxBroj = max(lista)
    izlaz.write('{0} {1} \n'.format(int(minBroj), int(maxBroj)))
ulaz.close()
izlaz.close()