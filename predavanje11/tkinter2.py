from tkinter import Tk, Button, Label, messagebox

def prikaziObavijest(vrijednost):
    messagebox.showinfo("HELLO", "Pritisnuli ste tipku 'HELLO'"+str(vrijednost))

glavni = Tk()

oznaka = Label(glavni, text="Ime osobe:", relief="raised")
oznaka.pack()

tipka = Button(glavni, text="Hello", command=lambda:prikaziObavijest(4))
tipka.pack()

glavni.mainloop()

