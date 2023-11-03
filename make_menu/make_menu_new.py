#Make_menu module
def menu_lists(win_size, ver, horz,t):
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in range(4):
           
        t.forward(win_size)
        t.left(90)
    traz=win_size-ver
    traz_horz=win_size-horz
    t.penup()
    t.goto(traz,traz_horz)
    t.pendown()
    t.write("اضافه کردن عدد به لیست (a", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz_horz-horz)
    t.pendown()
    t.write("حذف کردن عدد از لیست(b", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz_horz-horz*2)
    t.pendown()
    t.write("نمایش کل داده های لیست(c", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz_horz-horz*3)
    t.pendown()
    t.write("ذخیره داده های موجود در لیست روی حافظه دائم رایانه(d", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz_horz-horz*4)
    t.pendown()
    t.write("خروج(e", align='right', font=('Btitr', 10, 'bold'))


    
