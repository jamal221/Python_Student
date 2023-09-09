#برنامه ای بنویسید که تعداد اضلاع شکل و تعداد تکرار آن را از ورودی دریافت و سپس طرح کامل را ترسیم کند. از دستورات
import turtle
t1=turtle.Turtle()
shape_z=int(input("تعداد اظلاغ را وارد نماييد"))
shape_num=int(input("تعداد شکل را وارد نماييد"))
angle1=360/shape_z
angle2=360/shape_num
# width, color, speed
# زوج ها يه رنگ براي فرد رنگ ديگه
for i in range(shape_num):
    for j in range(shape_z):
        t1.forward(50)
        t1.left(angle1)
    t1.left(angle2)
