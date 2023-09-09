#Function
import random
def min_3(a,b,c):
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    print(min)
def min_3_new():
    a=int(input("عدد اول را وارد نماييد"))
    b=int(input("عدد دوم را وارد نماييد"))
    c=int(input("عدد سوم را وارد نماييد"))
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    print(min)
def min_3_new_good():
    a=int(input("عدد اول را وارد نماييد"))
    b=int(input("عدد دوم را وارد نماييد"))
    c=int(input("عدد سوم را وارد نماييد"))
    min_3(a,b,c)
def list_100():
    list1=list()
    for i in range(20):
        list1.append(random.randint(0, 9))
    return list1
        
    
