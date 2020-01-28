import logging
logging.basicConfig(filename="predavanje13/app.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
loger = logging.getLogger("MojLogger")

try:
    vrijednost = int(input("Unesi datum u veljači:"))
    assert 0 < vrijednost < 29, "unijeli ste pogrešan datum!"
except AssertionError as provjera:
    loger.critical(provjera)
    print(provjera)
    print("pripazite na datum")