mojset = {5,2,3,4,2,4,1}
for i in mojset:
    print(i, end=" ")

mojset.add(0)
print(mojset)

# mojset.update(8,7,4) # greška

mojset.update([8,7,4])
print(mojset)

mojset.remove(7)
print(mojset)

mojset.discard(7)
mojset.discard(5)
print(mojset)

mojset.pop()
print(mojset)

mojset.clear()
print(mojset)
