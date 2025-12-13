def functionArgs(*digits):
    sum=0
    for digit in digits:
        if digit%2==0:
            sum+=digit
    return sum
print(functionArgs(11,13,15,12,14,18))