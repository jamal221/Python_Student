import turtle
t1=turtle.Turtle()
shape=int(input("لطفا تعدا اظلاع را درج نماييد"))
shape_num=int(input("چه تعداد از اين شکل را مي خواهيد تکرار نماييد."))
angle1=360/shape
angle2=360/shape_num
for i in range(shape_num):
    for j in range(shape):
        t1.forward(50)
        t1.left(angle1)
    t1.left(angle2)
    
    
