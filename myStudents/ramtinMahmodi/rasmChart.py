import tkinter as tk
import random   
import turtle
# step 1     

def rasm():
    a=int(num1_Entry.get().strip())
    b=int(num2_Entry.get().strip())
    c=int(num3_Entry.get().strip())
    X=[]
    for i in range(100):
        number=random.randint(-100,100)
        X.append(number)  
     
    Y=[]
    for x in X:
        y=a*(x**2)+(b*x)+c
        Y.append(y)
    # در دستورات زیر دساگاه مخاصل=ات رسم می شود
    t1=turtle.Turtle()
    t1.speed(50)
    t1.pensize(10)
    t1.color('Red')
    t1.goto(-300,0)
    t1.forward(600)
    t1.penup()
    t1.goto(0,200)
    t1.pendown()
    t1.right(90)
    t1.forward(400)

    t1.pensize(3)
    t1.penup()
    t1.goto(X[0],Y[0])
    t1.pendown()
    t1.color("black")
    t1.circle(0.1)
    # t1.fillcolor()
    
    for i in range(100):
         t1.penup()
         t1.color("black")
         t1.goto(X[i],Y[i])
         t1.pendown()
         t1.circle(0.1)
         print(f"(x:{X[i]},y:{Y[i]}) ")
         


    


rasm_window=tk.Tk()   
rasm_window.title('برنامه پیدا کردن مختصات نقطه ها') 
# ---------------------
tk.Label(rasm_window,text='y=ax+yباشد،لطفاً a,b را درج نماییداگر معادله ی خط به صورت').grid(row=0,column=1,pady=5,padx=5)  
# ---------------------
tk.Label(rasm_window,text='a').grid(row=1,column=0,pady=5,padx=0)
num1_Entry=tk.Entry(rasm_window)
num1_Entry.grid(row=1,column=1,pady=5,padx=0)  
# ---------------------
tk.Label(rasm_window,text='b').grid(row=2,column=0,pady=5,padx=1)
num2_Entry=tk.Entry(rasm_window)
num2_Entry.grid(row=2,column=1,pady=10,padx=1) 
# ---------------------
tk.Label(rasm_window,text='c').grid(row=3,column=0,pady=5,padx=1)
num3_Entry=tk.Entry(rasm_window)
num3_Entry.grid(row=3,column=1,pady=10,padx=1)
# ---------------------
btnMaghsum=tk.Button(rasm_window,text='رسم',command=rasm)
btnMaghsum.grid(row=4,column=1,pady=10,padx=10) 
# ---------------------
rasm_window.mainloop()