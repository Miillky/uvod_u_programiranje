class Automobil:
    def __init__(self, pocVr1 = 150, pocVr2 = 'zelena'):
        self.Brzina = pocVr1
        self.Boja = pocVr2
    def vrati_specifikacije(self):
        podaci = "Max brizina je {0}, Boja je {1}".format(self.Brzina, self.Boja)
        return podaci

a1 = Automobil()
print(a1.vrati_specifikacije())

a2 = Automobil(233, 'crna')
print(a2.vrati_specifikacije())

a3 = Automobil(100)
print(a3.vrati_specifikacije())