dat = open('predavanje10/for.txt', 'w')
dat.write('Prvi red\nDrugi red\nTrećo red')
dat.close()

dat = open('predavanje10/for.txt', 'r')
for i in dat:
    print(i)

dat = open('predavanje10/for.txt', 'r')
for i in dat:
    for j in i:
        if not j=='\n':
            print(j, end=' ')
        else:
            print(j, end='')