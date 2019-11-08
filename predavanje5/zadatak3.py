# Napišite program koji traži unos riječi, zatim sve samoglasnike minje iz malog u veliko slovo
a=str(input("Unesi riječ: "))
a=a.replace("a","A")
a=a.replace("e","E")
a=a.replace("i","I")
a=a.replace("o","O")
a=a.replace("o","U")
print(a)