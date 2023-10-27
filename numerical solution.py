import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x,t)
def f(x,t):
    # Define the constants
    m = 10000 # Mass of the particle
    E = 10 # Total energy of the particle
    G = 6.6743e-11 # Gravitational constant
    M = 5.9722e24 # Mass of the central body
    # Return the value of f(x,t)
    return np.sqrt(2/m * (E + G*M*m/x))

# Define the initial condition
t0 = 0 # Initial time
x0 = 1 # Initial position

# Define the final time
tf = 20 # Final time

# Define the number of steps
n = 1000 # Number of steps

# Define the step size
h = (tf - t0)/n # Step size

# Create an array of time points
t = np.linspace(t0, tf, n+1)

# Create an array to store the values of x
x = np.zeros(n+1)

# Set the initial value of x
x[0] = x0

# Apply the Runge-Kutta method
for i in range(n):
    # Calculate the intermediate values
    k1 = h * f(x[i], t[i])
    k2 = h * f(x[i] + 0.5 * k1, t[i] + 0.5 * h)
    k3 = h * f(x[i] + 0.5 * k2, t[i] + 0.5 * h)
    k4 = h * f(x[i] + k3, t[i] + h)
    # Update the value of x
    x[i+1] = x[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plot the solution
plt.plot(t, x, label='Runge-Kutta solution')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint
#
# # Constants
# G = 6.67430e-11  # Gravitational constant (m^3 kg^(-1) s^(-2))
# m = 100000  # Mass of the particle (kg)
# E = -1.0  # Total energy of the particle (Joules)
# M = 5.9722e26
#
# # Define the function representing the differential equation
# def func(y, t):
#     x, v = y
#     dxdt = v
#     dvdt = np.sqrt(2 / m * (E + G * M * m / x))
#     return [dxdt, dvdt]
#
#
# # Initial conditions
# y0 = [1.0, 0.0]  # Initial position and velocity
# t = np.linspace(0, 10, 1000)  # Time values for integration
#
# # Solve the differential equation using odeint
# sol = odeint(func, y0, t)
#
# # Extracting the results
# x, v = sol[:, 0], sol[:, 1]
#
# # Plotting the results
# plt.figure(figsize=(8, 6))
# plt.plot(t, x, label='Distance from center (x)')
# plt.plot(t, v, label='Velocity (v)')
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.legend()
# plt.grid(True)
# plt.show()
