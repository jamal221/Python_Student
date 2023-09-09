#بحث متغيير ها

#print(type(Code_meli))
#Yekan_meli=Code_meli%10
#print(Yekan_meli)

#num1=int(input("عدد اول"))
#num2=int(input("عدد دوم"))
#print(f"{num1}//{num2}:  ",num1//num2)
#print(f"{num1}/{num2}:  ",num1/num2)
#eq1=2-8*(15//8)**3-4+2
#print(eq1)

def cehck_meli():
    try:
        
        Code_meli=int(input("کد ملي را وارد نماييد"))
        Yekan_meli=Code_meli%10
        if (Yekan_meli==0 or Yekan_meli==1):
            print("روز شنبه مراجعه نماييد")
        if (Yekan_meli==2 or Yekan_meli==3):
            print("يکشنبه")
        if (Yekan_meli==4):
            print("دوشنبه")
        if (Yekan_meli==5):
            print("سشنبه")
        if (Yekan_meli in [6,7,8] ):
            print("چهار شنبه")
        if (Yekan_meli in [9] ):
            print("پنجشنبه")
    except:
        print("کد ملي را به درستي درج نماييد")
def print_even(a):
    list1=list()
    for i in range(2,a+1,2):
        list1.append(i)
    return list1
        
