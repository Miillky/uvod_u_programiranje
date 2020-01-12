# Napišite program koji u tatoteku "Z1.txt" upisuje brojeve od 100 do 200, svaki broj u novi red.
dat = open("predavanje10/Z1.txt", "w")
for i in range(100,200):
    dat.write(str(i)+'\n')
dat.close()