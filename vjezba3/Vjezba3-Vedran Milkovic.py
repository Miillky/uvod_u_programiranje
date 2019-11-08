print('Python je baš cool!\nKažu da je programski jezik\nPython dobio naziv po seriji "Monthy Python",\nto je baš zanimljivo.')

v1 = int( input("Unesite stranicu a:") )
v2 = int( input("Unesite stranicu b:") )
print("Opseg pravokutnika je: ", 2*v1+2*v2)

v1 = int( input("Unesite stranicu a:") )
v2 = int( input("Unesite stranicu b:") )
print("Opseg pravokutnika je: ", v1*v2)

v1 = int( input("Unesite stranicu kvadrata n:") )
print("Površina kvadrata je: ", v1**2)

v1 = int( input("Unesite cijenu pernice n: ") )
v2 = int( input("Unesite iznos od bake m:") )
print("Ivana od dojeda treba dobiti", v1-v2, "kuna")

v1 = int( input("Ocjena iz predmeta 1:") )
v2 = int( input("Ocjena iz predmeta 2:") )
v3 = int( input("Ocjena iz predmeta 3:") )
v4 = int( input("Ocjena iz predmeta 4:") )
v5 = int( input("Ocjena iz predmeta 5:") )
print("Prosjek ocjena iz predmeta je:", (v1+v2+v3+v4+v5)/5)

v1 = int( input("Unesite prirodan broj a:") )
v2 = int( input("Unesite priroda broj b:") )
print(v1, " + ", v2, "=", v1+v2)
print(v1, " - ", v2, "=", v1-v2)
print(v1, " * ", v2, "=", v1*v2)

v1 = int( input("Unesite iznos kredita:") )
v2 = int( input("Unesite godišnju kamatu:") )
v3 = int( input("Unesite broj mjeseci kredita:") )
print("Kamata je:", (v1*v2*(v3+1))/2400)

v1 = int( input("Unesite broj dana:") )
v2 = int( input("Unesite broj sati:") )
v3 = int( input("Unesite broj minuta") )
v4 = int( input("Unesite broj sekundi") )
print(v1, " dana ", v2, " sati ", v3, " minuta i ", v4, " sekundi je ", v1*24*60*60+v2*60*60+v3*60+v4, " sekundi")

v1 = int( input("Unesite broj sekundi:") )
print(v1, " sekundi je ", ( (v1//60)//60)//24, " dana ", ((v1//60)//60)%24, " sati ", (v1//60)%60, " minuta i ", v1%60, " sekundi" )

print("Unesite početak filma:")
v1 = int( input("Sat:") )
v2 = int( input("Minuta:") )
v3 = int( input("Sekunda:") )
print("\nUnesite kraj filma:")
v4 = int( input("Sat:") )
v5 = int( input("Minuta:") )
v6 = int( input("Sekunda:") )
vp = v1*3600+v2*60+v3
vk = v4*3600*v5*60+v6
vr=vk-vp
print("Film je trajao ", ((vr//60)//60)%24, " sati ", (vr//60)%60, " minuta i ", vr%60, " sekundi")