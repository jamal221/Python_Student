
list1=list()
def  view_odd():
    try:
        
        a=int(input(":لطفا عدد را وارد کنيد "))
        s=0
        print ("اعداد اول از يک تا ",a)
        print("")
        for i in range (a) :
            if (i%2==1):
                list1.append(i)
                #print (i)
                s=s+i
        print(list1)
        print ("جمع اعداداول داخل ليست ","=",s) 
        print("")
        return list1
    except:
        print("فقط اعداد را واردکنيد")
    
def R_list(list1):
    list2=list()
    print("چاپ معکوس ليست :")
    print("") 
    
    for i in range (len (list1)-1,-1,-1):
        #print(list1[i])
        list2.append(list1[i])
    print (list2)

        
def make_s () :
    import turtle
    t=turtle.Turtle()
    try:
        
        t.pensize(10)
        x=int(input("لطفا تعداد مربع ها را وارد کنيد: "))
        for i in range(x):
            if (i%2==1):
                t.pencolor("red")
            else :
                t.pencolor("black")
            for j in range (4):
                t.forward(100)
                t.left(90)
            t.left(360/x)
    except:
         print("تعداد مربع فقطبا اعدادواردشود")
        
