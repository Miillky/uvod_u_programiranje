# Definirajte funkciju koja će na osnovi koeficijenata kvadratne funkcije vraćati True ako funkcija čiji su parametri zadani ima relne nul-točke, inače će vratiti False.
# Napišite fi glavnu main() funkciju koja prikazuje poziv s nekim brojevima, te osigurajte da se program ne pokrene prilikom importa

import math

def provjKvaFun(a,b,c):
    izraz = b**2 - 4*a*c
    if izraz > 0:
        return True
    else:
        return False

def main():
    print(provjKvaFun(a,b,c))

if __name__ == "__main__":
    main()