import turtle
import random
t1=turtle.Turtle()
t2=turtle.Turtle()
shape=int(input("لطفا تعدا اظلاع را درج نماييد"))
shape_num=int(input("چه تعداد از اين شکل را مي خواهيد تکرار نماييد."))
angle1=360/shape
angle2=360/shape_num
t2.penup()
t2.forward(100)
t2.pendown()
for i in range(shape_num):
    #r=random.random()
    #g=random.random()
    #b=random.random()
    #t1.fillcolor((r,g,b))
    #t1.begin_fill() 
    for j in range(shape):
        t1.forward(50)
        t1.left(angle1)
        t2.forward(50)
        t2.left(angle1)
    t1.end_fill()  
    t1.left(angle2)
    t2.end_fill()  
    t2.left(angle2)
    
