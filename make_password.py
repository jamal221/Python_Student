# توليد رمز از نام و نام خانوادگي
def gen_pass():
    name=input("لطفا نام را وارد نماييد")
    family=input("لطفا نام خانوادگي را درج نماييد")
    harf1=name[0].upper()
    harf2=family[0].lower()
    harf3=str(ord(name[0]))
    harf4=str(ord(name[2])-ord(family[0]))
    harf5="A"
    harf6="_"
    harf7=family[0].upper()
    harf8=str(ord(family[-3]))
    password=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8
    print(password)
    
                       

