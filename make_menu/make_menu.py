#Make_menu
def make_menu_funtion(win_size,t):
    t.penup()
    t.goto(0,0)
    t.pendown()
    for i in range(4): 
        t.forward(win_size)
        t.left(90)
    t.penup()
    dist=30
    traz=win_size-dist
    t.goto(win_size-dist,traz)
    t.pendown()
    t.write("اضافه کردن عدد به لیست (a", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz-dist)
    t.pendown()
    t.write("حذف کردن عدد از لیست(b", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz-2*dist)
    t.pendown()
    t.write("نمایش کل داده های لیست(c", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz-3*dist)
    t.pendown()
    t.write("ذخیره داده های موجود در لیست روی حافظه دائم رایانه(d", align='right', font=('Btitr', 10, 'bold'))

    t.penup()
    t.goto(traz,traz-4*dist)
    t.pendown()
    t.write("خروج(e", align='right', font=('Btitr', 10, 'bold'))
