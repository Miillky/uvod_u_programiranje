class Automobil:
    doseg = "650"
    def __init__(self, pocVr1 = 150, pocVr2 = 'zelena'):
        self.Brzina=pocVr1
        self.Boja = pocVr2
        self.doseg = "450"
    def metoda2(self):
        return self.doseg

a1 = Automobil()
print(a1.doseg)

print(a1.metoda2())

del a1.doseg
print(a1.doseg)

print(a1.metoda2())

a1.doseg = "1000"
print(a1.doseg)