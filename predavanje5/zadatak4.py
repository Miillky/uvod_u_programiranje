# Napišite program koji traži unos riječi, zatim iza svakog samoglasnika u toj riječi dodaje znak $ te na kraju ispisuje riječ
unos=str(input("Unesi riječ: "))
rezultat=""
for i in unos:
    rezultat = rezultat + i
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        rezultat = rezultat + "$"
print(rezultat)