# Napišite program koji traži unos riječi, zatim umjesto prvog samoglasnike pište tekst "<1>",
# umjesto drugog "<2>", umjesto trećeg "<3>" itd.
unos=str(input('Unesi riječ: '))
br, rezultat=1,""
for i in unos:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        rezultat = rezultat + "<" + str(br) + ">"
        br+=1
    else:
        rezultat = rezultat + i

print(rezultat)