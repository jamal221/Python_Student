#lambda
import random
#b=int(input("عدد مورد نظر را وراد نماييد"))
pow3=lambda a:(a**2)*a
#print(pow3(b))

def list_pow3():
    list1=list()
    list2=list()
    for i in range(10):
        rnds=random.randint(0,9)
        list2.append(rnds)
        num=pow3(rnds)
        list1.append(num)
    #print (list2)
    return (list1)
    
