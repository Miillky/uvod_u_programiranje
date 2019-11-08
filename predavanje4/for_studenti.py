# Napišite program kojim će se unositi ocjene za n studenata te ispisati prosječnu ocjenu iz predmeta:
n=int(input("Unesi broj studena n:"))
zbrojOcjena = 0
for x in range(1, n+1):
    o = int(input("Unesite ocjenu {0}. studenata:".format(x)))
    zbrojOcjena += o
print("Prosječna ocjena na predmetu iznosi:", zbrojOcjena/n)