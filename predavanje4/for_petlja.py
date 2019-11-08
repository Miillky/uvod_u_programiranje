for x in range(1, 11):
    print(x, end=" ")

for x in range(20, 9, -1):
    print(x)

tekst="Hello World"
for x in tekst:
    print(x)

n=int(input("Unesite prirodan broj n:"))
zbroj = 0
for x in range(1, n+1):
    zbroj += x
print("Zbroj iznosi: ", zbroj)
