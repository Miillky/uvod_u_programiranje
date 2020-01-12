# Definiran je rjecnik s parovima ime_osobe:pin_kartice rj = {"Branka":3241, "Stipe":5623, "Doris":3577, "Ana":7544}
# Napišite program koji od korisnika prima ime osobe, a zatim traži pin. Ukoliko je unesen ispravan pin, korisnik unosi novi pin koji se pohranjuje u rječniku

rj = {'Branka':3241,'Stipe':5623,'Doris':3577,'Ana':7544}
ime = str(input("Unesi ime: "))
pin = rj[ime.capitalize()]
pin_in = int(input("Unesite pin: "))
if pin == pin_in:
    pin_in = int(input("Unesite novi PIN: "))
    rj.update({ime.capitalize():pin_in})
else:
    print("PIN neispravan!")