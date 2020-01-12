from tkinter import Tk, Canvas, Label

glavni = Tk()

c1 = Canvas(glavni, bg="blue", height=200, width=200)
c1.pack(side="right", expand=1, fill="both")

c2 = Canvas(glavni, bg="red", height=200, width=200)
c2.pack(side="right", expand=1, fill="both")

c3 = Canvas(glavni, bg="green", height=200, width=400)
c3.pack(side="left", expand=1, fill="both")

c4 = Canvas(glavni, bg="yellow", height=200, width=200)
c4.pack(side="bottom", expand=1, fill="both")

oznaka = Label(c1, text="Ime osobe:", relief="raised" )
oznaka.pack()

glavni.mainloop()