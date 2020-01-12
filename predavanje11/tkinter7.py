from tkinter import Tk, Canvas, Label

glavni = Tk()

c1 = Canvas(glavni, bg="blue", height=200, width=400)
c1.pack(expand=1, fill="both")

c2 = Canvas(glavni, bg="red", height=200, width=400)
c2.pack(expand=1, fill="both")

c3 = Canvas(glavni, bg="green", height=200, width=400)
c3.pack(expand=1, fill="both")

c4 = Canvas(c1, bg="yellow", height=200, width=200)
c4.pack(side="left", expand=1, fill="both")

c5 = Canvas(c2, bg="pink", height=200, width=200)
c5.pack(side="left", expand=1, fill="both")

c6 = Canvas(c3, bg="orange", height=200, width=200)
c6.pack(side="left", expand=1, fill="both")

c7 = Canvas(c3, bg="white", height=200, width=200)
c7.pack(side="left", expand=1, fill="both")

glavni.mainloop()