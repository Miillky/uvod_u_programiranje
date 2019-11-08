print("Dobar dan svijete!")
print("Vedran Milković")
print("1 2 3 4 5 6 7 8 9 10")
print(1,2,3,4,5,6,7,8,9,10, sep="\n")

#sa ASCII znakovima
print( "(\\-----/)", "  \\o o/  ", "   \\ /   ", "    o    ", sep="\n" )

#ASCII decimalni brojevi u znakove
prviRed = [40,92,45,45,45,45,45,47,41]
prviRed = ''.join(map(chr, prviRed))

drugiRed = [32,32,92,111,32,111,47,32,32]
drugiRed = ''.join(map(chr, drugiRed))

treciRed = [32,32,32,92,32,47,32,32,32]
treciRed = ''.join(map(chr, treciRed))

cetvrtiRed = [32,32,32,32,111,32,32,32,32]
cetvrtiRed = ''.join(map(chr, cetvrtiRed))

print(prviRed, drugiRed, treciRed, cetvrtiRed, sep="\n")