class Automobil:
    doseg = "650"
    def __init__(self, pocVr1 = 150, pocVr2 = 'zelena'):
        self.Brzina = pocVr1
        self.Boja = pocVr2
    def vrati_specifikacije(self):
        pod="Max brzina je {0}, Boja je {1}".format(self.Brzina, self.Boja)
        return pod
    def vrati_specifikacije2(self, istinitost):
        pod = "Brzina {2} {0}, Boja {2} {1}".format(self.Brzina,self.Boja, istinitost)
        return pod
    def metoda1(self):
        return # doseg
    def metoda2(self):
        return self.doseg


a1 = Automobil()
print(a1.vrati_specifikacije())
print(a1.vrati_specifikacije2("nije")) # greška jer specifikac
# print(a1.metoda1()) # greška jer deseg nije definiran (nije korišten self.doseg)
print(a1.metoda2())