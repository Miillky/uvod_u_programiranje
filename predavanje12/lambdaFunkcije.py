zbroj = lambda a,b:a+b
zbroj(2,3) #5

sljedbenik = lambda x:x+1
sljedbenik(5) #6

kvadrat = lambda x:x*x
kvadrat(3) #9

broj = lambda s:int(s)
broj('123')

prvi = lambda a:a[0]
prvi([1,2,3,4]) #1

d={'Audi':10, 'BMW':13, 'Honda':15, 'Toyota':8}
print(d)
d = sorted(d.items(), key=lambda x: x[1])
print(d)