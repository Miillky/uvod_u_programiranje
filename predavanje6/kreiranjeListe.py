for i in range(20):
    print(i, end=' ')

for i in range(10, 20):
    print(i, end=' ')

L_1 = [' ' for i in range(10)]
print(L_1)

L_2 = [0 for i in range(10)]
print(L_2)

import random
L_4 = [random.randint(10,20) for i in range(100)]
print(L_4)

lista = [i for i in range(2, 1001, 2)]
print(lista)

lista_1 = [1,2,3,4,5,6,7,8,9]
for broj in lista_1:
    print(broj, end='')