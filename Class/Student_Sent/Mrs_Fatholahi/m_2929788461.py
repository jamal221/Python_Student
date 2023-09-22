
#اجراي ماژول
#تابع اول
def view_odd(a):
    list1=list()
    for i in range(1,a+1,2):
        list1.append(i)
    return list1
    print(" نمايش مجموع اعداد ليست") 
    print(sum(print2))

#تابع ذوم
def R_List(print2):
 for i in range(len(print2)):
    last_item=print2.pop()
    print2.insert(i,last_item)
    print(print2[i])
    
print("نمابس ليست معکوس") 
print3=R_List(print2)

 #رسم شگل مربغ
import turtle
t1=turtle.Turtle()
t1.width(5)
t1.color("red")

for i in range(8):
    if i%2==0:
        t1.color("blue")
        for j in range(4):
            t1.forward(200)
            t1.left(90)
    else:
        t1.color("red")
        for j in range(4):
            t1.forward(200)
            t1.left(90)
    t1.left(45)
    
#رسم شکل آخر
import turtle
t1=turtle.Turtle()
shape_z=int(input("تعداد اضلاع را وارد تماييد"))
shape_num=int(input("تعداد شک را وارد کنيد"))
angle1=360/shape_z
angle2=360/shape_num

#t1.color("red")

for i in range(shape_num):
    if i%2==0:
        t1.color("blue")
        t1.width(10)
        for j in range(shape_z):
            t1.forward(50)
            t1.left(angle1)
    else:
        t1.color("green")
        t1.width(5)
        for j in range(shape_z):
            t1.forward(50)
            t1.left(angle1)
    t1.left(angle2)     
               
  
               
