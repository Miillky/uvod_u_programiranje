# d - cijeli broj
# 13d - cijeli broj koji zauzima sveukupno 13 znakova u tekstu
# 8s - string koji zauzima sveukupno 8 znakova
# 10f - realni broj koji zauzima 10 znakova u tekstu uključujući decimalnu točku (decimalni dio će biti prikazan sa 6 znamenaka ukoliko nije drugačije navedeno)
# 10.2f - realni broj koji zauzima 10 znakova u tekstu, decimale su prikazane s dvije znamekne

a=56.3
b="helikopter"
c=15
d=355.234
print("Prva je {0:0.2f}, druga je {1:2s}, treca je {2:1d}, cetvrta je {3:0.2f}".format(a, b, c, d))
print("Prva je {0:10f}, druga je {1:15s}, treca je {2:5d}, cetvrta je {3:0.4f}".format(a, b, c, d))
print("Prva je {0:15f}, druga je {1:20s}, treca je {2:d}, cetvrta je {3:15.4f}".format(a, b, c, d))
print("Prva je {0:f}, druga je {1:s}, treca je {2:d}, cetvrta je {3:0.1f}, prva je {0:0.0f}".format(a, b, c, d))