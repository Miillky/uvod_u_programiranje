from tkinter import Tk, Button, Entry, Label, messagebox

def prikaziObavijest(vrijednost):
    messagebox.showinfo("HELLO", "Pritisnuli ste tipku 'HELLO'"+str(vrijednost))

glavni = Tk()

oznaka = Label(glavni, text="Ime osobe:", relief="raised")
oznaka.pack()

unos = Entry(glavni, bd=5) #bd - debljina okvira
unos.pack()

unos2 = Entry(glavni, bg="green", width=7)
#bg - boja polja: width - širina
unos2.pack()

tipka = Button(glavni, text="Hello", command=lambda:prikaziObavijest(4))
tipka.pack()

glavni.mainloop()