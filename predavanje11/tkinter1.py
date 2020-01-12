from tkinter import Tk, Button, messagebox

def prikaziObavijest(vrijednost):
    messagebox.showinfo("HELLO", "Pritisnuli ste tipku 'HELLO'"+str(vrijednost))

glavni = Tk()
tipka = Button(glavni, text="Hello", command=lambda:prikaziObavijest(4))
tipka.pack()
glavni.mainloop()