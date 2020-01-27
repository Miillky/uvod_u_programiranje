import math

def izracun(x,y):
    if x+3 <= 0 or (y+3)**2 == 0:
        print('Greška')
        return -1

    return abs( math.cos(y)**4 + math.sqrt(x+3) )**3 / (y+3)**2

def main():
    x = int(input('Unesi prvi broj x: '))
    y = int(input('Unesi prvi broj y: '))
    return izracun(x, y)

if __name__ == "__main__":
    main()