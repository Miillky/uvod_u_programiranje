d = {'Dacia':10, 'Audi':8, 'BMW':12, 'Aston Martin':11}

print(sorted(d))
print(sorted(d.items()))

# sortiranje po vrijednosti - moramo definirati dodatnu funkciju
def usporedba(t):
    return t[1]

print(sorted(d.items(), key=usporedba))

string="4321"
lista=[4,3,2,1]
ntorka=(4,3,2,1)
rjecnik={"4":"travanj","3":"ozujak","2":"veljaca","1":"sijecanj"}

print(sorted(string))
print(sorted(lista))
print(sorted(ntorka))
print(sorted(rjecnik.items()))
