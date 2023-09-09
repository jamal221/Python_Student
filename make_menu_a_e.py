def design_menu(t):
    t.pencolor("green")
    t.penup()
    t.goto(230,200)
    t.pendown()
    t.write("اضافه کردن عدد به لیست (a", align='right', font=('Btitr', 15, 'bold'))

    t.penup()
    t.goto(230,170)
    t.pendown()
    t.write("حذف کردن عدد از لیست(b", align='right', font=('Btitr', 15, 'bold'))

    t.penup()
    t.goto(230,140)
    t.pendown()
    t.write("نمایش کل داده های لیست(c", align='right', font=('Btitr', 15, 'bold'))

    t.penup()
    t.goto(230,110)
    t.pendown()
    t.write("ذخیره داده های موجود در لیست روی حافظه دائم رایانه(d", align='right', font=('Btitr', 15, 'bold'))

    t.penup()
    t.goto(230,80)
    t.pendown()
    t.write("خروج(e", align='right', font=('Btitr', 15, 'bold'))
