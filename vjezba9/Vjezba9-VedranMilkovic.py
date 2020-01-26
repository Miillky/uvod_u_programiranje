def zbroji(a, b):
    c = a+b
    print('Rezultat je', c)

zbroji(5,3)

def ponmozi():
    a = int(input('Unesi 1. broj: '))
    b = int(input('Unesi 2. broj: '))
    c = a * b
    print('Umnožak brojeva je', c)

ponmozi()


def faktorijela(n):
    rez = 0
    for i in range(n):
        rez += i * n
    return rez

broj = 4
print('Faktorijela broja {0} je: {1}'.format(broj, faktorijela(broj)))


def ispis_a():
    print('funkcija a')

def ispis_b():
    print('funkcija b')

def ispis_c(x):
    print('funkcija c je primila parametar {0}'.format(x))

def vrati(x):
    return x

ispis_a()
ispis_b()
ispis_c(99)
print(vrati(99))

def kvadJed():
    from math import sqrt
    while True:
        a = int(input('Unesite parametar a: '))
        if a == 0:
            print('Parametar a mora biti zazličit od 0')
            continue

        b = int(input('Unesite parametar b: '))
        c = int(input('Unesite parametar c: '))

        korijen = b**2 - 4 * a * c
        if korijen < 0:
            print('Izraz b^2-4ac ne smije biti manji od 0')
            continue

        return (-b + sqrt(korijen))/(2*a)


print(kvadJed())

def parniNeparniZbroj(n):
    zbrojParnih = 0
    zbrojNeparnih = 0
    for i in range(1, n+1):
        broj = int(input('Unesite {0}. prirodan broj: '.format(i)))
        if broj % 2 == 0:
            zbrojParnih += broj
        else:
            zbrojNeparnih += broj

    print('Zbroj parnih brojeva = {0}, dok je zbroj neparnih brojeva = {1}'.format(zbrojParnih, zbrojNeparnih))

parniNeparniZbroj(5)

def sekMin(sek):
    return sek // 60

def sekSat(sek):
    return sekMin(sek) // 60

def sekDan(sek):
    return sekSat(sek)//24

sekunde = int(input('Unesite broj sekundi: '))
print('{0} sekundi je jednako {1} dana, {2} sata, {3}, minuta i {4} sekunde.'.format(sekunde, sekDan(sekunde), sekSat(sekunde)%24, sekMin(sekunde)%60, sekunde%60  ))
