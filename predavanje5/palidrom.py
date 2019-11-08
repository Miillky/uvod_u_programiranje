# Napiši program koji za zadanu riječ provjerava je li palidrom (primjeri: RATAK, KAPAK, KISIK...)
s='ratar'
p=''
for i in range(len(s)):
    p=s[i]+p
if p==s:
    print('Riječ je palindrom')