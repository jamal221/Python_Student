#Turten Nest for
import turtle
t=turtle.Turtle()
def draw_shape():
    for i in range(8):
        if(i % 2==0):
            t.pencolor("blue")
            t.pensize(10)
        else:
            t.pencolor("green")
            t.pensize(5)
        for j in range(4):
           t.forward(100)
           t.left(90)
        t.left(45)


draw_shape()
