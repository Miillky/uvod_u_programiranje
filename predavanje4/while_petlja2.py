# Napišite program koji računa srednju visinu učenika u razredu:
n = int(input('Upisite broj učenika u razredu: '))
zbroj = 0.0
i=0
while i < n:
    broj=float(input('Unesi visinu {0}. učenika: '.format(i+1)))
    zbroj+=broj
    i+=1
print('\nSrednja visina učenika je {0:0.2f}'.format(zbroj/n))