class tenisica():
    proizvodac = 'ne'
    velicina = 40
    cijena = 300
    akcija = 'ne'
t1 = tenisica()
print(t1.velicina)
# del t1.velicina - ne možemo izbrisat zato jer je vrijednost varijavble dio klase (default-na vrijednost)
t1.velicina = 38
print(t1.velicina)
del t1.velicina # možemo izbrisat jer smo postavili novu varijable, pa kad izbrišemo vrati se na vrijednost iz klase
print(t1.velicina)

class tenisica2():
    def __init__(self, proizvodac='adidos', velicina=39, cijena=305, akcija='ne'):
        self.proizvodac = proizvodac
        self.velicina = velicina
        self.cijena = cijena
        self.akcija = akcija

t2 = tenisica2()

print(t2.proizvodac) #adidos - zato jer je to defaultni parametar konstruktora
# del t2.velicina - ne možemo izbrisat vrijednost koja je definirana u constructoru klase
print(t2.velicina)

class tenisica3():
    def __init__(self, proizvodac='adidos', velicina=39, cijena=305, akcija='ne'):
        self.proizvodac = proizvodac
        self.velicina = velicina
        self.cijena = cijena
        self.akcija = akcija

    def akcija_switch(self):
        if self.akcija == 'ne':
            self.akcija = 'da'
            self.cijena = self.cijena * ((100-15)/100)

        else:
            self.akcija = 'ne'
            self.cijena = self.cijena * 1.1765

t3 = tenisica3()

t3.akcija_switch()
print("{0:0.2f}".format(t3.cijena))
t3.akcija_switch()
print("{0:0.2f}".format(t3.cijena))

class tenisica4():
    def __init__(self, proizvodac='adidos', velicina=39, cijena=305, akcija='ne'):
        self.proizvodac = proizvodac
        self.velicina = velicina
        self.cijena = cijena
        self.akcija = akcija
        self.posto = 100
    def akcija_switch(self, posto):
        if self.akcija == 'ne':
            self.akcija = 'da'
            self.cijena = self.cijena * ((100-posto)/100)
        else:
            self.akcija = 'ne'
            self.cijena = self.cijena * (100/(100-posto))

t4 = tenisica4()
t4.akcija_switch(15)
print("{0:0.2f}".format(t4.cijena))
t4.akcija_switch(15)
print("{0:0.2f}".format(t4.cijena))

from tkinter import *
class semafor():
    def __init__(self):
        self.glavni = Tk()
        self.c1 = Canvas(self.glavni, bg='red', height=100, width=100)
        self.c1.pack()
    def zuta(self):
        self.c1.configure(bg='yellow')
    def crvena(self):
        self.c1.configure(bg='red')
    def zelena(self):
        self.c1.configure(bg='green')

def main():
    s1 = semafor()
    return s1

main = main()