import pathlib
path = pathlib.Path().absolute()

dat = open('{0}/predavanje10/abeceda.txt'.format(path), 'r' )
dat.seek(2)
print(dat.readline(), end="")
dat.seek(dat.tell()+3)
print(dat.readline(), end="")
print(dat.read(), end="")
dat.close()