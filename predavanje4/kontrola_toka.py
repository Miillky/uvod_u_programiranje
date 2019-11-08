# Napišite program koji od korisnika traži onos jednog slova.
# Program će zatim provjeriti na kojem se mjestu u tekstu prvi put pojavljuje to slovo.
# Ako je slovo pronađeno, program ispisuje poziciju slova i prekida izvođenje.
# Tekst neka glasi "vrijeme sutra je promjenjivo i nestabilno"
slovo = str(input("Unesite slovo za pretragu: "))
tekst = "vrijeme sutra je promjenjivo i nestabilno"
pozicija=1
pronadeno=False

for s in tekst:
    if s==slovo:
        print("pozicija slova u tekstu je: ", pozicija)
        pronadeno = True
        break
    pozicija+=1

if pronadeno==False:
    print("slovo nije pronađeno")