#Definite Integrals
from scipy.integrate import quad
from numpy import sin,cos,tan
# Define your function here
def f(x):
  return cos(x)**3+3*(1/tan(x))  # Replace this with your actual function
# Define your limits a and b
a = 0  # Replace with your actual value
b = 15  # Replace with your actual value
# Calculate the integral
integral, error = quad(f, a, b)
print(f"The integral of f(x) from cos(x)**3+3*tan(x) is:  {a} to {b} is: {integral}")
print(f"Estimate of the absolute error in the result: {error}")

