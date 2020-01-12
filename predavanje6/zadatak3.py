# Napišite program koji ima zadane 2 liste i provjerava da li u te dvije liste postoje isti elementi.
# Ispisuje True ili False ovisno orezultatu usporedbe
flag = False
L1 = [1,2,3,4]
L2 = [2,5,7,9]
for pom in L1:
    if pom in L2:
        flag=True
print(flag)