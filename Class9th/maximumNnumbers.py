# برنامه محاسبه ماکزیمم سه عدد و مشان دادن با printf

def max3Digits(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    print(f"maximum {a}, {b} and {c} is: {max}")

# max3Digits(5,9,12)
    
def maxMultiDigits(*num):
    max=0
    for number in num:
        if number>max:
            max=number
    return max

print(f" maximum the numbers is: {maxMultiDigits(1,5,8,9)}")

