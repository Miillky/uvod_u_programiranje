# 25 == 17 False
# 15 > 17 False
# 18 <= 18 True
# 9 != 13 True

# True and False False
# True and not False True
# True or False and True True
# not false and not True or False False

# 2<3 and 3>4 False
# 4<5 and 4>=5 False
# 2+5 < 5+3 and 2-3 < 5-3 True
# 2>3 or 2<3 and not 2+3==3 True

n1 = int( input("Unesite prvi broj:") )
n2 = int( input("Unesite drugi broj:") )
if n1 >= 0 and n1%1==0 or n2>=0 and n2%1==0:
    if n1>n2:
        print("Veći je: ", n1)
    elif n2>n1:
        print("Veći je: ", n2)
    else:
        print("Niti jedan nije veći")
else:
    print("Uneseni broj nije prirodan")

n1 = int( input("Unesite prirodan broj N:"))
if not n1>=0 or not n1%1==0:
    print("Uneseni broj nije prirodan")
else:
    if n1%2==1:
        print("Broj je neparan")
    else:
        print("Broj je paran")

n1 = int(input("Unesite prirodan broj N:"))
if not n1>0 or not n1%1==0:
    print("Uneseni broj nije prirodan")
else:
    if n1%7==0:
        print("Broj je djeljiv sa 7")
    else:
        print("Broj nije djeljiv sa 7")

n1 = int(input("Unesite cijeli broj:"))
if n1 == 0:
    print("Broj je 0")
elif n1>0:
    print("Broj je pozitivan")
elif n1<0:
    print("Broj je negativan")

n1 = float(input("Unesite pH vrijednost:"))
if n1>0 and n1<=4.5:
    print("pH vrijednost: 'Jako kisela'")
elif n1>4.5 and n1<=6.5:
    print("pH vrijednost: 'Slabo kisela")
elif n1>6.5 and n1<=7.5:
    print("pH vrijednost: 'Neutralna'")
elif n1>7.5 and n1<=9.5:
    print("pH vrijednost: 'Slabo lužnata'")
elif n1>9.5 and n1<=14:
    print("pH vrijednost: 'Jako lužnata'")
else:
    print("pH vrijednost izvan raspona!")

n1 = float(input("Unesite realan broj:"))
if(n1>100 and n1<=200) or (n1>=500 and n1<=1000):
    print("Broj se nalazi UNUTAR intervala <100,200] U [500,1000]")
else:
    print("Broj se nalzi IZVAN intervala <100,200 U [500,1000]")

n1 = float(input("Unesite postotak riješenosti ispita [0-100]:"))
if(n1>=0 and n1<=50):
    print("Ocjena je nedovoljna")
elif(n1>50 and n1<=63):
    print("Ocjena je dovoljan")
elif(n1>63 and n1<=76):
    print("Ocjena je dobar")
elif(n1>76 and n1<=89):
    print("Ocjena je vrlo dobar")
elif(n1>89 and n1<=100):
    print("Ocjena je odličan")
else:
    print("Postotak izvan raspona")

n1 = int(input("Unesite prvi broj:"))
n2 = int(input("Unesite drugi broj:"))
n3 = int(input("Unesite teci broj:"))
if not n1>=0 or not n1%1==0 or not n2>=0 or not n2%1==0 or not n3>=0 or not n3%1==0:
    print("Uneseni broj nije prirodan")
else:
    if n1>n2 and n1>n3:
        print("Najveći je: ", n1)
    elif n2>n1 and n2>n3:
        print("Najveći je: ", n2)
    elif n3>n1 and n3>n2:
        print("Najveći je: ", n3)
    else:
        print("Niti jedan nije najveći")