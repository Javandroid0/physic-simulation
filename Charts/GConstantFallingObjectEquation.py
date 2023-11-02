# import numpy
# import numpy as np
#
# m = 10000  # mass of the falling ball in kg
# E = 0  # energy of the falling ball in J
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24
# x = 100
# t = 5
# theta = numpy.arccos(np.sqrt((-E * x)/m *M *G))
# c1 = (m * M * G)/(-E) ** (3/2)
# c2 = theta + np.sin(theta) * np.cos(theta)
# c1 * c2 = np.sqrt(2/m)


# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define the constants
# m = 10000  # mass of the falling ball in kg
# E = -1  # energy of the falling ball in J
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24
#
#
# # Define the functions
# def theta(x):
#     #print(x)
#     ans1 = np.sqrt((-E * x))
#     ans2 = (m * M * G)
#     ans3 =ans1 / ans2
#     print(ans3)
#     answer = np.arccos(ans3)
#     #print(answer)
#     return answer
#
# print(np.arccos(-0.9))
#
# def c1():
#     return (m * M * G) / (-E) ** (3 / 2)
#
#
# def c2(x):
#     return theta(x) + np.sin(theta(x)) * np.cos(theta(x))
#
#
# def t(x):
#     return (c1() * c2(x)) / np.sqrt(2 / m)
#
#
# # Define the range of x values
# x_values = np.linspace(0, 1e-8, 1000)
#
# # Plot t as a function of x
# # plt.plot(x_values, t(x_values))
# # plt.xlabel('x')
# # plt.ylabel('t')
# # plt.title('t vs. x')
# # plt.show()


#
# import numpy as np
# import sympy
# import matplotlib.pyplot as plt
#
# # Define the variables
# E, x, m, M, G = sympy.symbols('E x m M G')
# theta = sympy.acos(sympy.sqrt((-E * x) / (m * M * G)))
# c1 = (m * M * G) / (-E) ** (3/2)
# c2 = theta + sympy.sin(theta) * sympy.cos(theta)
# t = (c1 * c2) / sympy.sqrt(2 / m)
#
# # Expand the expression for t
# expanded_t = sympy.expand(t)
#
# # Create a numpy array of x values
# x_values = np.linspace(-10, 10, 100)
# print(expanded_t)
# # Create a numpy array of t values by substituting x_values into the expanded expression for t
# t_values = [float(expanded_t.subs(x, x_value)) for x_value in x_values]
#
# # Plot t vs. x
# plt.plot(x_values, t_values)
# plt.xlabel('x')
# plt.ylabel('t')
# plt.title('Plot of t vs. x')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# import sympy as sym
#
# m = 1e3  # mass of the falling ball in kg
# E = -1  # energy of the falling ball in J
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24
#
# x = np.linspace(-10, 10, 100)
#
# c1 = np.sqrt(-E * x / m * M * G)
# c2 = m * M * G / (-E) ** 3 / 2
# z1 = sym.series(sym.sin(c1), x0=0, n=10)
# z2 = sym.series(sym.sin(c1), x0=0, n=10)
# radic = np.sqrt(2 / m)
# t = c2 * c1 + c2(z1 * z2)
# t = t / radic
#
# plt.plot(x, t)
# plt.xlabel('x')
# plt.ylabel('t')
# plt.title('Plot of t vs x')
# plt.show()


# import sympy
#
# x = sympy.Symbol('x')
# f = sympy.acos(x)
# taylor = f.series(x, 0, 5).removeO()
#
# sympy.plotting.plot(f, taylor, (x, 0, 10), title='Taylor series expansion of arccos(x) from 0 to 10')



# import matplotlib.pyplot as plt
# import numpy as np
#
# # Define the constants
# m = 1
# M = 1
# G = 6.6743e-11
# E = 1
#
#
# # Define the function x(t)
# def x(t):
#     return (m * M * G / E) / np.cos(np.sqrt(m * G * t / (2 * E)))
#
#
# # Create an array of time values
# t = np.linspace(0, 10, 1000)
#
# # Create an array of x values
# x_values = x(t)
#
# # Plot x vs t
# plt.plot(t, x_values)
#
# # Add labels and title to the plot
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('Plot of x vs t')
#
# # Show the plot
# plt.show()


# from scipy import integrate
# import numpy as np
#
# # Define the function to be integrated
# def integrand(x, E, m, M, G, t):
#     return 1 / np.sqrt(E + m * M * G / x) - np.sqrt(2 / m) * t
#
# # Constants
# E =  -1# Assign the value of E
# m =  1000# Assign the value of m
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24
# t = 5 # Assign the value of t
#
# # Numerically solve the integral
# result, _ = integrate.quad(integrand, 0, np.inf, args=(E, m, M, G, t))
#
# print("Numerical solution of the integral:", result)

#
# import numpy as np
# from scipy.integrate import quad
#
# # Define the constants
# E =  -1# Assign the value of E
# m =  1000# Assign the value of m
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24
#
# # Define the integrand
# def integrand(x):
#     return 1 / np.sqrt(E + m * M * G / x)
#
# # Define the limits of integration
# a = 0.0
# b = 10.0
#
# # Compute the integral using quad
# result, error = quad(integrand, a, b)
#
# # Compute t using the result of the integral
# t = np.sqrt(m / 2) * result
#
# print("The value of t is:", t)


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

E =  -1# Assign the value of E
m =  1000# Assign the value of m
G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
M = 5.9722e24

# Define the integrand
def integrand(x):
    return 1 / np.sqrt(E + m * M * G / x)

# Define the limits of integration
a = 0.1
b = 10000.0

# Compute the integral using quad
result, error = quad(integrand, a, b)

# Compute t using the result of the integral
t = np.sqrt(m / 2) * result

# Define the range of x values to plot
x_values = np.linspace(a, b, num=100)

# Compute the corresponding t values for each x value
t_values = []
for x in x_values:
    result, error = quad(integrand, a, x)
    t_values.append(np.sqrt(m / 2) * result)

# Plot t as a function of x
plt.plot(x_values, t_values)
plt.xlabel('x')
plt.ylabel('t')
plt.title('t as a function of x')
plt.show()
