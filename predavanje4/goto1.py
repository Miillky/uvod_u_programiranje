# Primjer 1: program koji traži od korisnika unos broja većeg od 5.
# Ako je uneseni broj veći od 5, ispisuje ga i prekida se izvođenje programa.
# U suprotnom ispisuje poruku o pogrešnp unesenom broju i ponovno traži unos broja.
from goto import with_goto

@with_goto
def primjer():
    label .pocetak
    a = int(input("Unesi broj veći od 5: "))
    if a > 5:
        print("broj je ",a)
    else:
        print("Broj mora biti veći od 5")
        goto .pocetak

primjer()