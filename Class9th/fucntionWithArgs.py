def functionArgs(*arg):
    sum1=0
    for digit in arg:
        if digit%2==0:
            sum1+=digit
    return sum1
# print(functionArgs(11,13,15,12,14,18,15,16,5))

def sumALl(*a):
    sum1=0
    for item in a:
        sum1+=item
    return sum1
# print(sumALl())

def showItems(**var):
    for key,value in var.items():
        # print(key,value)
        print(f"{key} is: {value}")

# showItems(name='jamal', family='azizbeigi', age='35')
x=100
print(f"the init value os x is {x}")
def scopeX():
    # x=50
    global x
    x=x+100
    print(f"then the result x is in first blobal function is: {x}")

scopeX()
def scopeX_again():
    global x
    # x=x+100
    x+=120
    print(f"finaly: the result x in call again is: {x}")

scopeX_again()
