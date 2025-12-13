from tkinter import *

def sumTwoDigits(a, b):
    return a + b

def calculate_total():
    # read entry values and convert to int
    a = int(E1.get())
    b = int(E2.get())

    # calculate sum
    result = sumTwoDigits(a, b)

    # clear E3 before inserting
    E3.delete(0, END)
    E3.insert(0, result)

top = Tk()
top.title("Adder")

L1 = Label(top, text="Physics")
L1.place(x=10, y=10)
E1 = Entry(top, bd=5)
E1.place(x=80, y=10)

L2 = Label(top, text="Maths")
L2.place(x=10, y=50)
E2 = Entry(top, bd=5)
E2.place(x=80, y=50)

L3 = Label(top, text="Total")
L3.place(x=10, y=150)
E3 = Entry(top, bd=5)
E3.place(x=80, y=150)

B = Button(top, text="Add", command=calculate_total)
B.place(x=100, y=100)

top.geometry("250x250+10+10")
top.mainloop()
