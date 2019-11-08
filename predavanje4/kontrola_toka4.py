# Napišite program koji ispisuje brojeve od 0 do 99, uz iznimku da ne ispisuje 33, 44 i 55.
for i in range(100):
    if i==33:
        continue
    if i==44:
        continue
    if i==55:
        continue
    print(i)

for i in range(100):
    if i==33 or i==44 or i==55:
        continue
    print(i)