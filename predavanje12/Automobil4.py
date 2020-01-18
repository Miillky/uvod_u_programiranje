class Automobil:
    doseg = "850"
    def __init__ (self, pocVr1 = 150, pocVr2 = 'zelena'):
        self.Brzina = pocVr1
        self.Boja = pocVr2
        self.doseg = "750"
    def metoda2(self):
        return self.doseg

a1 = Automobil()
print(a1.metoda2())