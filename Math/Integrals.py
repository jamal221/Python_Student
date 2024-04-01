from sympy import symbols, integrate, sin, cos, tan,cot
# Define the variable
x = symbols('x')
# Define the function you want to integrate
f = cot(x)**2+3*tan(x)  
# Calculate the indefinite integral
F = integrate(f, x)
print(f"The indefinite integral of f(x) is: {F} + C")
