#Create My Math Modal

from sympy import symbols, diff, lambdify, sin, cos, tan, integrate
from scipy.integrate import quad

import numpy as np
from numpy import sin, cos, tan
import matplotlib.pyplot as plt

# Define the variable
x = symbols('x')

def indefinte_Inetgrals(f):
    # Calculate the indefinite integral
    F = integrate(f, x)
    return F


def definite_Integrals(your_Lambda_function, low_val, up_val):
    
    # Calculate the integral
    res=list()
    integral, error = quad(your_Lambda_function, low_val, up_val)
    res.append(integral)
    res.append(error)
    return res

def Diff_function(your_function, your_val):
    from numpy import sin,cos,tan
    # Calculate the derivative
    f_Diff = diff(your_function, x)
    # Define val to find definite value
    val_Diff=f_Diff.subs(x,your_val)
    res=list()
    res.append(f_Diff)
    res.append(val_Diff)
    return res

def Diff_function_pure(your_function):
    #derivative
    from sympy import  diff,lambdify
    # Calculate the derivative
    f_Diff = diff(your_function, x)
    return f_Diff


def plot_you(your_function_lambda, low_val, up_val):
    from numpy import sin,cos,tan
    #Plot
    import matplotlib.pyplot as plt
    # Define your interval [a, b]
    a = low_val  # Start of the interval
    b = up_val  # End of the interval
    # Generate an array of x values from a to b
    x_values = np.linspace(a, b, 300)  # 100 points between a and b
    # Calculate the y values based on the function f(x)
    y_values = your_function_lambda(x_values)
    # Plot the function
    plt.plot(x_values, y_values, label="your_function")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of the function f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()



# Define the symbolic variable

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sin, cos, tan

# Define the symbolic variable
x = symbols('x')

def plot_diff_and_main(your_function_str, low_val, up_val):
    # Convert the string to a symbolic expression
    your_function_sym = eval(your_function_str, {'x': x, 'sin': sin, 'cos': cos, 'tan': tan})

    # Differentiate symbolically using your Diff_function_pure (assuming it's correct)
    diffed_function_sym = diff(your_function_sym, x)

    # Convert symbolic expressions to callable functions
    your_function = lambdify(x, your_function_sym, modules=['numpy'])
    diffed_function = lambdify(x, diffed_function_sym, modules=['numpy'])

    # Define your interval [a, b]
    a = float(low_val)  # Start of the interval
    b = float(up_val)   # End of the interval

    # Generate an array of x values from a to b
    x_values = np.linspace(a, b, 300)

    # Calculate the y values based on the function f(x)
    y_values = your_function(x_values)
    y_values_diff = diffed_function(x_values)

    # Plot the function
    plt.plot(x_values, y_values, color='red', label="main_function")
    plt.plot(x_values, y_values_diff, color='blue', label="Diffed_function")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of the function f(x) and its derivative')
    plt.legend()
    plt.grid(True)
    plt.show()
