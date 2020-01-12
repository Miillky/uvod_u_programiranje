import pathlib
path = pathlib.Path().absolute()

dat = open('{0}/predavanje10/IzlaznaDatoteka.txt'.format(path), 'w' )
# dat.write('Zapisujem tekst')

lista1 = ['Kata', 'Suzana', 'Domagoj']
lista2 = ['Pero\n', 'Janko\n', 'Ivona\n']
dat.writelines(lista1)
dat.writelines(lista2)
dat.close()

# datoteka se ponovno otvara i unosi se novi sadržaj (w)
dat = open('{0}/predavanje10/IzlaznaDatoteka.txt'.format(path), 'w' )
lista3 = ['Pero\n', 'Janko\n']
dat.writelines(lista3)
dat.close()

# datoteka se ponovno otvara i unosi se dodatni sadržaj (a)
dat = open('{0}/predavanje10/IzlaznaDatoteka.txt'.format(path), 'a' )
lista3 = ['Pero\n', 'Janko\n']
dat.writelines(lista3)
dat.close()