# Napišite program koji računa te ispisuje plaću radnika na temelju sljedećih podataka:
# Cijena radnog sata
# Broj sati koje je radnik radio

cijenaSata=float(input('Unesi cijenu sata [kn]:'))
brojSati=float(input('Unesi broj sati:'))
placa=cijenaSata*brojSati
print('Placa ranika iznosi', placa, 'kn')