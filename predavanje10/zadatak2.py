# Napišite program koji iz datoteke "Z2.txt" učitava brojeve koji su zapisani kako je navedeno nako zadataka, prevara ih u brojeve te ispisuje u uvećane za 1.
dat = open("predavanje10/Z2.txt", "r")
retci = dat.readlines()
for s in retci:
    print("{}".format(int(s)+1))
dat.close()