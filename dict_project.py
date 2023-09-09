#Dictionery
dict1=dict()
dict1['car']="C8"
dict1['brand']="Benz"
print(dict1)
dict1['car1']="b5"
dict1['brand1']="BMW"
print(dict1)
print(dict1.values())
print(dict1.keys())
set1=set()
list1=list()
for i in range(10):
    list1.append(i)
list1[1]=2
list1[2:5]=[5,5,5]
print(list1)
set1=set(list1)
print(set1)

print(len(list1)-len(set1))
