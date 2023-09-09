import turtle
t1=turtle.Turtle()
inc=0
for i in range(10):
    for j in range(4):
        t1.forward(100+inc)
        t1.left(90)
    inc=inc+30
