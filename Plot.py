#Plot
import numpy as np
from numpy import sin
import matplotlib.pyplot as plt
# Define your function here
def f(x):
  return sin(x)**5-4*sin(x)**3+3*sin(x)  # Example: f(x)=x^5-4x^3+3x
# Define your interval [a, b]
a = -10  # Start of the interval
b = 10  # End of the interval
# Generate an array of x values from a to b
x_values = np.linspace(a, b, 300)  # 100 points between a and b
# Calculate the y values based on the function f(x)
y_values = f(x_values)
# Plot the function
plt.plot(x_values, y_values, label='f(x) = x^5-4x^3+3x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x)')
plt.legend()
plt.grid(True)
plt.show()
