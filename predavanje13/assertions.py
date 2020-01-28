# javljanje greške kada je unesen krivi datum
vrijednost = int(input("Unesi datum u veljači:"))
assert 0 < vrijednost < 29, "unijeli ste pogrešan datum!"

try:
    vrijednost = int(input("Unesi datum u veljači:"))
    assert 0 < vrijednost < 29, "unijeli ste pogrešan datum!"
except AssertionError:
    print("pripazite na datum")

try:
    vrijednost = int(input("Unesi datum u veljači:"))
    assert 0 < vrijednost < 29, "unijeli ste pogrešan datum!"
except AssertionError as provjera:
    print(provjera)
    print("pripazite na datum")