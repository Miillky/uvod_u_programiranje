from tkinter import Tk, Canvas

glavni = Tk()
glavni.geometry("800x400") #zadajemo veličinu glavnog prozora pošto se on ne prilagodi automatski veličini svojih widgeta

c1 = Canvas(glavni, bg="blue")
c1.place(height=200, width=400)

c2 = Canvas(glavni, bg="red")
c2.place(x=400,height=200, width=400)

c3 = Canvas(glavni, bg="green")
c3.place(y=200,height=200, width=400)

c4 = Canvas(glavni, bg="yellow")
c4.place(x=400,y=200,height=200, width=400)
#pomoću opcija x i y zadajemo udaljenost od gornjeg lijevog kuta nad-prozora ili widgeta