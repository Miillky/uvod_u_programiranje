def g(a,b):
    if a // 10 % 10 > b // 10 % 10:
        return True
    else:
        return False

print(g(17,10))
print(g(28,11))
print(g(156,81))