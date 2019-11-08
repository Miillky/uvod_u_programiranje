print('Program za provjeru unesenog broj:')
broj = int(input("Unesi priroda broj:"))
if broj<0:
    print('Broj {0} je negativan'.format(broj))
elif broj==0:
    print('Broj {0} je nula'.format(broj))
else:
    print('Broj {0} je pozitivan'.format(broj))