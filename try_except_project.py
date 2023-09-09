#try except
import Code_meli
flag=0
try:
    a=int(input("لطفا کد ملي را به صورت 10 رقمي وارد نماييد"))
    print(Code_meli.check_meli(a))
    flag=1
except:
    print("شما غير کد ملي را وارد نموده ايد")
    flag=0
finally:
    if flag==0:
        print("در اجراي برنامه خطايي روي داده است")
    else:
        print("برنامه به درستي اجرا شد")
    
