import types

jabuka = types.SimpleNamespace(
    vrsta="idared",
    boja="crvena",
    tezina=89
)
print(jabuka.vrsta)
print(jabuka.boja)
print(jabuka.tezina)

jabuka.versta = "granny smith"
del jabuka.boja
jabuka.tezina = 125

print(jabuka.vrsta)
print(jabuka.tezina)

print(type(jabuka))
print(type(jabuka.vrsta))
print(type(jabuka.tezina))