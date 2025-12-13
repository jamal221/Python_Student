def maximum(a,b,c):
    max=a
    if(b>max):
        max=b
    if(c>max):
        max=c
    return max
# a=int(input('insert the first number'))
# b=int(input('insert the second number'))
# c=int(input('insert the third number'))
# print(f"maximum {a} and {b} and {c} is the number: {maximum(a,b,c)}")

def maximumALL(*args):
    max=0
    for number in args:
        if number>max:
            max=number
    return max
print(maximumALL(1,5,8,10))
