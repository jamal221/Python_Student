#Check odd or even
num1=input("لطفا عدد را وارد نماييد")
even=0
odd=0
try:
    
    for i in range(len(num1)):
        if(int(num1[i])%2)==0:
            even+=1
        else:
            odd+=1
    print("تعداد ارقام زوج برابر است با:   ",even)
    print("تعداد ارقام فرد برابر است با:   ",odd)
except:
    print("لطفا در درج ارقام دقت نماييد")

        
    
