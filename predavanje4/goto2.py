# Primjer 2: program koji traži od korisnika unos broja većeg od 5.
# Ako je uneseni broj veći od 5, ispisuje ga i prekida se izvođenje programa.
# U suprotnom ispisuje poruku o pogrešnp unesenom broju i ponovno traži unos broja.
while True:
    a=int(input("Unesi broj veći od 5: "))
    if a>5:
        print("Broj je ", a)
        break
    else:
        print("Broj mora biti veći od 5")
        continue