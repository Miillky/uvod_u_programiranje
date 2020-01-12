import pathlib
path = pathlib.Path().absolute()

dat = open('{0}/predavanje10/MojaDatoteka.txt'.format(path) )

#print(dat.read())
print(dat.readline())
print(dat.readline())
print(dat.readline())
print(dat.readline())

dat = open('{0}/predavanje10/MojaDatoteka.txt'.format(path), 'r' )
print(dat.readlines())

print(dat.seek(10))
print(dat.readline())

print(dat.tell())
print(dat.seek(dat.tell() + 7))