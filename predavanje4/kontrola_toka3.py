# U slučaju više ugniježdenih prelji, prekinut će se samo ona u kojoj se break nalazi

for i in range(3):
    for j in range(3):
        for k in range(3):
            if k==1:
                break
            print(i,j,k)