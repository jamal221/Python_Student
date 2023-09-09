import keyboard
def read_a(t, list1):
    
    if keyboard.read_key() == "a":
        t.clear()
        t.pencolor("red")
        t.penup()
        t.goto(230,200)
        t.pendown()
        t.write("لطفا عدد يا حرفي را جهت درج در ليست وارد نماييد", align='right', font=('Btitr', 15, 'bold'))
        your_key=""
        while keyboard.read_key() != "enter":
            your_key+=keyboard.read_key()        
        list1.append(your_key)
        t.pencolor("black")
        t.penup()
        t.goto(230,180)
        t.pendown()
        t.write(list1, align='right', font=('Btitr', 12, 'bold'))

        t.pencolor("blue")
        t.penup()
        t.goto(230,260)
        t.pendown()
        t.write("بازگشت به منوي اصلي با حرف m", align='right', font=('Btitr', 12, 'bold'))
