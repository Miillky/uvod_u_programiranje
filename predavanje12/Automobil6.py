class Autmobil:
    Brzina = 330
    Boja = 'roza'
    doseg = "650"
    def metoda2(self):
        return self.doseg

a1 = Autmobil()
print(a1.metoda2())

print(a1.Brzina)

print(a1.Boja)

print(a1.doseg)

#del a1.Brzina # greška jer nismo postavili vrijednost atributa Brzina

print(a1.Brzina)

a1.Brzina = 278
print(a1.Brzina)

del a1.Brzina # možemo izbrisati jer smo postavili vrijednost atributu Brzina sa a1.Brzina = 278
print(a1.Brzina)