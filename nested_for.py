import turtle
t1=turtle.Turtle()
t1.width(5)
t1.color("red")

for i in range(8):
    if i%2==0:
        t1.color("blue")
        for j in range(4):
            t1.forward(50)
            t1.left(90)
    else:
        t1.color("red")
        for j in range(4):
            t1.forward(50)
            t1.left(90)
    t1.left(45)
