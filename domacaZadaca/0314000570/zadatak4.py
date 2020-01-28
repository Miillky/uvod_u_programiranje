#Napišite klasu lift. Konstruktor klase postavlja atribut objekta (trenutni_kat = 1).
# Zatim napisite metodu pozovi_lift. Metoda prima argument koji predstavlja željeni (odredišni) kat lifta.
# Metoda zatim ispisuje smjer kretanja lifta (gore ili dolje) na temelju atributa trenutni_kat i parametra zeljeni_kat te metode. Na kraju se trenutni_kat postavlja u željeni kat.
# U programu instancirajte jedan objekt te klase te prikažite korištenje metode.

class lift():
    def __init__(self, trenutni_kat = 1):
        self.trenutni_kat = trenutni_kat

    def pozovi_lift(self, zeljeni_kat):
        if zeljeni_kat > self.trenutni_kat:
            print('Gore')
        if zeljeni_kat < self.trenutni_kat:
            print('Dolje')
        if zeljeni_kat == self.trenutni_kat:
            print('Trenutni kat')
        self.trenutni_kat = zeljeni_kat

lift = lift()
lift.pozovi_lift(1)
lift.pozovi_lift(20)
lift.pozovi_lift(20)
lift.pozovi_lift(2)