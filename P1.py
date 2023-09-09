count=0
while count<=3:
    try:
        a=int(input('لطفا کد ملي را وارد نماييد'));
        b=a%10;
        #print(type(a))
        def check1(b):
            if b%2==0:
                print("لطفا شنبه مراجغه نماييد")
            else:
                print("لطفا يکشنبه مراجعه نماييد")
        check1(b)
        count+=1
    except ValueError:
        print("شما غير از کد ملي را وارد نموده ايد لطفا يکبار ديگر سعي نماييد")
        count+=1
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    
        
