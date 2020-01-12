# Napišite program koji od korisnika prima string i provjerava da li se string nalazi u listi:
# L5 = ['stol', 'brava', 'kvaka']
# Program ispisuje poruku da li se riječ nalazi ili ne nalazi u listi

L5 = ['stol','brava','kvaka']
tekst = str(input('unesite tekst za provjeru: '))
if tekst in L5:
    print('Riječ se nalazi u listi')
else:
    print('Riječ se ne nalazi u listi')