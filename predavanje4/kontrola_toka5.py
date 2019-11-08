#U slučaju više ugnježdenih preltji, prekinut će se samo jedna iteracija petlje u kojoj se continue nalazi.
for i in range(3):
    for j in range(3):
        for k in range(3):
            if k==1:
                continue
            print(i,j,k)