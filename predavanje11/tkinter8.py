from tkinter import Tk, Canvas, Label

glavni = Tk()

c1 = Canvas(glavni, bg="blue", height=200, width=400)
c1.grid(row=1,column=1)

c2 = Canvas(glavni, bg="red", height=200, width=400)
c2.grid(row=1,column=2)

c3 = Canvas(glavni, bg="green", height=200, width=400)
c3.grid(row=2,column=1)

c4 = Canvas(glavni, bg="yellow", height=200, width=200)
c4.grid(row=2,column=2)

c5 = Canvas(glavni, bg="pink", height=200, width=200)
c5.grid(row=2,column=3)

c6 = Canvas(glavni, bg="orange", height=200, width=200)
c6.grid(row=3,column=1)

c7 = Canvas(glavni, bg="white", height=200, width=200)
c7.grid(row=3,column=2)

glavni.mainloop()