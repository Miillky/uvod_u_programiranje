from tkinter import Tk, Button, Entry, Label, IntVar, Checkbutton, Spinbox, Radiobutton, messagebox

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

V1 = IntVar()
C1 = Checkbutton(glavni, text="Prihvaćam uvjete", variable=V1, onvalue=1, offvalue=0, height=5, width=20)
C1.pack()

V3=IntVar()
S1=Spinbox(glavni, textvariable=V3, from_=5, to=10)
S1.pack()

V2 = IntVar()
R1 = Radiobutton(glavni, text="SES", variable=V2, value=1)
R1.pack()

R2 = Radiobutton(glavni, text="RAC", variable=V2, value=2)
R2.pack()

R3 = Radiobutton(glavni, text="MEH", variable=V2, value=3)
R3.pack()

glavni.mainloop()