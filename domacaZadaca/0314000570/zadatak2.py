# Napišite program koji od korisnika unosi 2 prirodna broja(i provjerava da li su prirodni) i
# aritmetički operator između njih(+,-,* ili /). Program ispisuje rezultat ovisno o unesenim
# brojevima i operaciji između njih.

a = int(input('Unesite prvi prirodan broj: '))

if a < 0 and a%1==0:
    print('Uneseni broj nije prirodan')

op = input('Unesite jedan od operatora +,-,*, /: ')

b = int(input('Unesite drugi prirodan broj: '))

if b < 0 and b%1==0:
    print('Uneseni broj nije prirodan')


if op == '+' or op == '-' or op == '*' or op == '/':
    if op == '+':
        print(a+b)
    if op == '-':
        print(a-b)
    if op == '*':
        print(a*b)
    if op == '/':
        print(a/b)
