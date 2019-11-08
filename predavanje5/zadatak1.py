# Napišite program koji će od korisnika tažiti unos dvije riječi, te zatim provjeriti i ispisati koja riječ je dulja.
a=str(input('Unesi prvu riječ: '))
b=str(input('Unesi drugu riječ: '))
if len(a) > len(b):
    print('Riječ', a, "je dulja")
elif len(a) < len(b):
    print('Riječ', a, "je dulja")
else:
    print('Obje riječu su iste duljine')