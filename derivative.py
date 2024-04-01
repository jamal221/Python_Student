#derivative
from sympy import symbols, diff, sin
# Define the variable and function
x = symbols('x')
f = sin(x)**3 - 3*(sin(x)**2) + 2*sin(x)  # Replace with your actual function
# Calculate the derivative

f_Diff = diff(f, x)
# Define val to find definite value
val=45
val_Diff=f_Diff.subs(x,val)
print(f"The derivative of {f} is: {f_Diff}")
print(f"The val derivative of {f} in {val}  is: {val_Diff}")
