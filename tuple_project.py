#Tuple
tuple1=tuple()
print(type(tuple1))
list1=list(tuple1)
list1.append(5)
tuple1=tuple(list1)
print(tuple1)
list1=list(tuple1)
for i in range(10):
    list1.append(i)
tuple1=tuple(list1)
print(tuple1)
print(tuple1[2])
print(tuple1[2:])
