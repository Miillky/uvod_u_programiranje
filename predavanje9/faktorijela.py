def faktorijela(n):
    fakt=1
    for i in range(1, n+1):
        fakt*=i
    return fakt

print(faktorijela(13))

import math
print(math.factorial(13))