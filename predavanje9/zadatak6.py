# Napišite funkcju koja generira deset slučajnih brojeva od 1 do 100 i ispisuje ih. Napišite i glavnu main() funkciju oka poziva vašu funkciju, te osgurajte da se program ne pokrene prilikom importa.

import random

def generiraj():
    for i in range(10):
        rBroj = random.randint(1,100)
        print('{0}\n'.format(rBroj))

def main():
    generiraj()

if __name__ == "__main__":
    main()