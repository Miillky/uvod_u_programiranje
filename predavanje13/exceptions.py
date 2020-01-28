# NameError
try:
    priintt("Hello World")
except:
    print("Pojava exception-a kod print-a")

# Očekivana vrsta exception-a
try:
    priintt("Hello World")
except NameError:
    print("Pojava exception-a kod print-a")

# Neče se izvršit jer smo stavili da je OSError exeption
""" try:
    priintt("Hello World")
except OSError:
    print("Pojava exception-a kod print-a") """

# SyntaxError - ne moćemo obraditi pomoću try except blokova jer iterpreter odbija izvođenje programa
""" try:
    print("jello there!!"))
except SyntaxError:
    print("Pojava exeption-a kod print-a") """

# else - multi except
try:
    priintt("Hello World")
except NameError:
    print("Pojava exeption-a kod print-a")
except OSError:
    print("Pojava OSEerror exception-a")
else:
    print("Everyting is fine")

# više očekivanih grešaka za jedan except blok
try:
    priintt("Hello World")
except (NameError, OSError):
    print("Pojava exception-a kod print-a")

# stvaranje exceptiona
try:
    print("Hello World")
    raise OSError
except (NameError, OSError):
    print("Pojava exception-a kod print-a")

# umjesto else-a, finally - izvršava se bez obzira da li se javi greška ili ne
try:
    priintt("Hello World")
except NameError:
    print("Pojava exception-a kod print-a")
finally:
    print("Ja se uvijek javljam!")

# primjer iznimke
try:
    vrijednost = int(input("Unesi broj:"))
except ValueError:
    print("Unesena pogrešna vrsta podataka!")
else:
    print("Unijeli ste: ", vrijednost)


