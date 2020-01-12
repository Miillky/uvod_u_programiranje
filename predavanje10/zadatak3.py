dat = open("predavanje10/Z3.txt", "r")
retci = dat.readlines()
for s in retci:
    print("{}{}{}".format(s[0], s[2], s[4], end=""))
dat.close()