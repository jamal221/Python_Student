# Turtle Text
import turtle
t=turtle.Turtle()
for i in range(4):
    t.forward(200)
    t.left(90)
t.penup()
t.goto(180,180)
t.left(180)
t.write("1: کليد a  را فشار دهيد", align='right')
