#The main module
try:
    try:
        def sum_odd():
            try:
                num1=int(input("لطفا عدد مورد نظر براي جمع اعداد فرد را وارد نماييد."))
                sum=0
                list1=list()
                list2=list()
                for i in range(1,num1+1,2):
                    sum+=i
                    list1.append(i)
                list2.append(sum)
                list2.append(list1)
                return list2
            except:
                print("ورودي را بررسي نماييد")
    except:
        print("ورودي را بررسي نماييد")
    def rev_list(list1):
        try:
            
            list2=list()
            for i in range(-1, -len(list1)-1,-1):
                list2.append(list1[i])
            return list2
        except:
            print("ورودي تابع دوم را هم بررسي نماييد")
except:
    print("کل وردي ها را بررسي نماييد")
def make_squre():
    import turtle
    t=turtle.Turtle()
    try:
        num_sq=int(input("لطفا تعدداد مربع ها را وارد نماييد"))
        t.color("green")
        t.pensize(5)
        for i in range(num_sq):
            if i%2==0:
                t.color("blue")
                t.pensize(10)
            else:
                
                t.color("green")
                t.pensize(5) 
                
            for j in range(4):
                t.forward(100)
                t.right(90)
            t.right(45)
    except:
        print("در درج ورودي مربع دقت نماييد")
                
    
