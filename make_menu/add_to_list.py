#make_menu_add_to_list
def addToListMenu(t, list1, num):
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in range(4):
           
        t.forward(300)
        t.left(90)
    t.penup()
    t.goto(270,270)
    t.pendown()
    t.write("لطفا عدد مورد نظر را درج نماييد", align='right', font=('Btitr', 10, 'bold'))
    list1.append(num)
