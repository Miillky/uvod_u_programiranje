# Napišite prelju koja se izvršava 100 puta ali prekida izvšenje nakon 50 iteracija.
for i in range(1, 100):
    if i==50:
        break
    print(i)