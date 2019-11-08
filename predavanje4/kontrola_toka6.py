# Napišite program koji od korisnika traži unos jednog slova.
# Program će zatim provjeriti koliko puta se u tekstu to slovo pojavljuje.
# Program ispisuje broj pojavljivanja unesenog slova i broj preostalih znakova u tekstu.
# Tekst neka glasi "vrijeme sutra je promjenjivo i nestabilno"
# Riješite problem korištenjem samo jende if provjere, bez elif i else
slovo = str(input("Unesite slovo za pretragu: "))
tekst = "vrijeme sutra je promjenjivo i nestabilno"

pojavljivanja=0
ostali=0

for s in tekst:
    if s==slovo:
        pojavljivanja+=1
        continue
    ostali+=1

print("Broj pojavjivanja unesenego slova: ", pojavljivanja)
print("Broj ostalih znakova: ", ostali)