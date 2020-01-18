# Napravite klasu kuca koja stvori objekt s atributima prozor i ulazna_vrata
# Svi atributi imaju inicijalnu vrijednost ‘zatvoreno’
# Zatim sa svaki atribut napraviti metodu koja će promijeniti stanje atributa iz ‘zatvoreno’ u ‘otvoreno’ i obrnuto
# Napraviti metodu koja će ispisati stanje atributa u obliku teksta: “Prozor je <zatvoreno/otvoreno>, Ulazna vrata je <zatvoreno/otvoreno>”

class kuca:
    def __init__(self, v='zatvoreno', p='zatvoreno'):
        self.ulazna_vrata = v
        self.prozor = p
    def promjena_ulazna(self):
        if self.ulazna_vrata == 'zatvoreno':
            self.ulazna_vrata = 'otvoreno'
        else:
            self.ulazna_vrata = 'zatvoreno'
    def promjena_prozor(self):
        if self.prozor == 'zatvoreno':
            self.prozor = 'otvoreno'
        else:
            self.prozor = 'zatvoreno'
    def kuca_status(self):
        print("Prozor je {0}, Ulazna vrata je {1}".format(self.prozor, self.ulazna_vrata))

k = kuca()
k.kuca_status()
k.promjena_ulazna()
k.kuca_status()
k.promjena_prozor()
k.kuca_status()