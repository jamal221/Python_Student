#شرط ها

Code_meli=int(input("لطفا کد ملي را درج نماييد"))
yekan=Code_meli%10
#print(yekan)
if yekan==0:
    print("لطفا روز شنبه مراجعه نماييد")
if yekan==1 or yekan==2:
    print("روز شما يک شنبه است")
if yekan==3:
    print("روز شما دوشنبه است")
if yekan==4 or yekan==5 :
    print("روز شما سشنبه است")
if yekan==6 or yekan==7 :
    print("روز شما چهار شنبه است")
if yekan==8 or yekan==9 :
    print("روز شما پنج شنبه است")

