import cv2

try:
    img = cv2.imread('oblici.png')

    cv2.line(img, (368, 247), (368 + round((490 - 368) / 2), 92), (0, 0, 255), 5)
    cv2.line(img, (368 + round((490 - 368) / 2), 92), (490, 247), (0, 0, 255), 5)
    cv2.line(img, (368, 247), (490, 247), (0, 0, 255), 5)
    cv2.rectangle(img, (83, 45), (250, 134), (0, 255, 0), 5)
    cv2.circle(img, (220, 300), 95, (255, 0, 0), -1)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print('Nepostojeća datoteka')


class slika():

    def __init__(self):
        self.img = cv2.imread('oblici.png')
        cv2.imshow('image', self.img)

    def trokut(self):
        cv2.line(self.img, (368, 247), (368 + round((490 - 368) / 2), 92), (0, 0, 255), 5)
        cv2.line(self.img, (368 + round((490 - 368) / 2), 92), (490, 247), (0, 0, 255), 5)
        cv2.line(self.img, (368, 247), (490, 247), (0, 0, 255), 5)
        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def pravokutnik(self):
        cv2.rectangle(self.img, (83, 45), (250, 134), (0, 255, 0), 5)
        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def krug(self):
        cv2.circle(self.img, (220, 300), 95, (255, 0, 0), -1)
        cv2.imshow('image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

import logging

logging.basicConfig(filename='zad5.log', filemode='w', format='%(message)s')
loger = logging.getLogger("")
try:
    vrijednost = int(input('Unesite težinu osobe:'))
    assert vrijednost > 0, 'Težina ne može biti manja od 0'
except AssertionError as AE:
    loger.warning(AE)
    print('Greška! Pogledajte log datoteku!')


class mikser_vode():
    toplina_vode = 0

    def hladna_voda(self):
        if self.toplina_vode == 0:
            self.toplina_vode = 1
        elif self.toplina_vode > 1:
            self.toplina_vode -= 1

    def topla_voda(self):
        if self.toplina_vode == 0:
            self.toplina_vode = 5
        elif self.toplina_vode < 5:
            self.toplina_vode += 1

    def zatvori(self):
        self.toplina_vode = 0
