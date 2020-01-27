import random

def loto645():
    return random.randint(1,45)

def main():
    brojevi = set()
    for broj in range(0,6):
        if len(brojevi) < 6:
            brojevi.add(loto645())

    print("Loto brojevi su:", ', '.join( str(broj) for broj in list(brojevi) ) )

if __name__ == "__main__":
    main()