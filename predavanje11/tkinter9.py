from tkinter import Tk, Canvas

glavni = Tk()

c1 = Canvas(glavni, bg="blue", height=200, width=400)
#height i width unutar Canvas naredbe nema utjecaj, te vrijednosti se postavljaju unutar place metode
c1.place(height=200, width=400)

c2 = Canvas(glavni, bg="red")
c2.place(height=200, width=400)

#plavi canvas se ne vidi jer je crveni preko njega
c3 = Canvas(glavni, bg="green", height=200, width=200)
c3.place()

#zeleni canvas se ne vidi jer mu nisu definirane širina i visina u metodi place

glavni.mainloop()