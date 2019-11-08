n=int(input('Upisite broj učenika u razredu: '))
zbroj=0.0
for i in range(n):
    broj=float(input('Unesi visinu {0}. učenika:'.format(i+1)))
    zbroj+=broj
print('\nSrednja visina učenika je {0:0.2f}'.format(zbroj/n))