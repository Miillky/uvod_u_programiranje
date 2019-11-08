# Napišite program koji preačunava unsene sekunde u sekunde, minute, sate i dane.
sekunde = int(input('Unesi sekunde:'))
ostatkSekunde = sekunde % 60
minute = sekunde // 60
ostatakMinute = minute % 60
sati = minute // 60
ostatakSati = sati % 24
dani = sati // 24
print('sekunde:', ostatkSekunde)
print('minute:', ostatakMinute)
print('sati:', ostatakSati)
print('dani:', dani)