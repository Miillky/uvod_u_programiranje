# Napišite program koji unosi prirodan broj n. Zatim napišite dvije različite funkcije, prva koja uvećava vrijednost varjable n za 5 globalno, dok druga uvećava vrijednost za 10 ali samo lokalno.
# Svaka od funkcija ispisuje vrijednost varijable nakon uvećavanja. Iz programa pozovite prvu funkciju, za drugu funkciju i na kraju ispišite vrijednost varijable n iz samog progama (iz main funkcije)

n=int(input("Unesi prirodan broj: "))

def prva():
    global n
    n+=5
    print("vrijednost u prvoj funkciji:", n)

def druga(n):
    n+=10
    print('vrijednost u drugoj funkciji:', n)

def main():
    prva()
    druga(n)
    print("vrijednost u glavnoj funkciji:", n)

main()