#Turtle
import turtle
tur=turtle.Turtle()
for i in range(4):
    tur.forward(200)
    tur.left(90)
tur.pencolor("blue")
tur.pensize(10)
tur.right(180)
for i in range(4):
    tur.forward(200)
    tur.left(90)

tur.pencolor("red")
tur.pensize(5)
tur.penup()
tur.goto(-200,-200)
tur.pendown()
for i in range(10):
    tur.forward(20)
    tur.left(360/10)

