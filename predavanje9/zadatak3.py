# Definirajte funkciju koje će pamtiti broj i provjeravati dali je broj prost. Funkcija vraća True ako je broj prost ili False ako nije

def prostBroj(broj):
    if broj == 1:
        return False
    for i in range(2,broj):
        if broj%i == 0:
            return False
        return True

print(prostBroj(20))