# Napišite program koji će ispisivati vrijeme na ančin koji je prikazan na slici.
# Svake sekunde se ispisuje jedan red.
# Ispis se zaustavlja nakon 2 minute i 59 sekundi.

from time import sleep

for i in range(0, 3):
    for j in range(0, 60):
        print(i, "minuta i", j, "sekundi")
        sleep(1)