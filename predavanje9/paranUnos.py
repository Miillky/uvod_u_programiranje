def paran(n):
    if n%2==0:
        print("Broj {0} je paran".format(n))
    else:
        print("Broj {0} je neparan".format(n))

paran(11)
paran(0)

def unos():
    a = int(input("Unesi prirodan broj: "))
    return a

paran(unos())