def Odd_num(n):
    oddlist=[]
    for i in range(n+1):
        if(i % 2 !=0):
            oddlist.append(i)
    return oddlist

def view_odd(n):
    sum_odd=0
    for i in range(n+1):
        if(i % 2 !=0):
            sum_odd += i
    return sum_odd

def reverse_odd(list):
    t = len(list)
    list2=[]
    for i in range(t-1,-1,-1):
        list2.append(list[i])
    return list2


            
