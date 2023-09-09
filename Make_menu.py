#Final Project
import make_menu_a_e
import turtle
t=turtle.Turtle()
list1=list()
import read_a_menu
import keyboard
#wind=t.screen
#wind.bgcolor("black")
#print(wind.screensize().width())
t.penup()
t.goto(-250,-250)
t.pendown()

for i in range(4):
    t.forward(500)
    t.left(90)
t.left(180)
make_menu_a_e.design_menu(t)
read_a_menu.read_a(t, list1)


if keyboard.read_key() == "m":
    t.clear()
    make_menu_a_e.design_menu(t)
    read_a_menu.read_a(t, list1)

    
#t.clear()


