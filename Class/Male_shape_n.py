# Designe Shape
import turtle
t=turtle.Turtle()
def make_shape():
    
    try:
        
        num_z=int(input("تعداد اظلاغ"))
        num_shape=int(input("تعداد شکل"))

        for i in range(num_shape):
            for j in range(num_z):
                t.forward(100)
                t.left(360/num_z)
            t.left(360/num_shape)
    except:
        print("در درج اعداد دقت نماييد")
