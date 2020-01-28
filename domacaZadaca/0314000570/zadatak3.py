# Napišite funkciju otvori_i_obrni koja prima ime datoteke u obliku stringa.
# Funkcija zatim otvara datoteku i čita sadržaj iz nje (pretpostavka je da se datoteka nalazi na istom mjestu kao i datoteka s izvornim kodom). Iz sadržaja datoteke izvlači riječi i pohranjuje ih u rječnik.
# Zatim čita riječi iz rječnika i pohranjuje ih u istu datoteku u obrnutom redoslijedu prepisujući preko starog sadržaja.
# Napišite i primjer poziva funkcije otvori_i_obrni u glavnom programu gdje joj se predaje ime datoteke „izvor.txt“ u kojoj se nalazi sadržaj:
# Krafna Sok Parmezan Mlijeko Tofu Datulje Ananas Kava

def otvori_i_obrni():
    inputFile = open('domacaZadaca/0314000570/izvor.txt', 'r')
    dictionary = {}
    for line in inputFile:
        dictionary = { i: line.split()[i] for i in range(0, len(line.split())) }

    inputFile.close()

    if dictionary:
        outputFile = open('domacaZadaca/0314000570/izvor.txt', 'w')
        for index in sorted(dictionary.keys(), reverse=True):
            outputFile.write(dictionary[index] + ' ')
        outputFile.close()

otvori_i_obrni()