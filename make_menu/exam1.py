import turtle
t=turtle.Turtle()
import make_menu_new
import add_to_list
make_menu_new.menu_lists(450, 15, 25,t)
import keyboard
while (keyboard.read_key()!="e"):
    
    if keyboard.read_key() == "a":
        t.clear()
        add_to_list.addToListMenu(t)
    if keyboard.read_key() == "m":
        t.clear()
        make_menu_new.menu_lists(450, 15, 25,t)
if keyboard.read_key() == "e":
    t.penup()
    t.clear()
    t.goto(200,0)
    t.pendown()
    t.write("شما با موفقيت از برنامه خارج شديد.", align='right', font=('Btitr', 20, 'bold'))


        

    
