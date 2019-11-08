s1='abcd'
s2='bcdefg'
s1+s2 # 'abcdbcdefg'
s1*2 # 'abcdabcd'
s1 in s2 # False
s1 not in s2 # True
s3='ab'
s3 in s1 # True

s="ABCDEFGH"
len(s) #8 - vraća duljinu stringa
min(s) # 'A' - vraća znak s najmanjom kodnom vrijenošću
max(s) # 'H' - vraća znak s najvećom kodnom vrijednošću
ord('A') # 65 - vraća kodni broj znaka
chr(65) # 'A' - vraća znak za broj koda
str(1000) # '1000' - vraća znakovni prikaz broja n