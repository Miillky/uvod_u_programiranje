import math
def MatIzraz(x,y):
    if x+y < 0 or x+y == 0:
        print("Krivi unos")
        return -1
    brojnik = math.sqrt(x+y)
    nazivnik = x+y
    z = brojnik / nazivnik
    return z

print(MatIzraz(5,5))
print(MatIzraz(0,0))
print(MatIzraz(-5,4))