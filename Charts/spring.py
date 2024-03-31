# Import the libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
m = 1 # mass in kg
k = 100 # spring constant in N/m
omega = np.sqrt(k/m) # angular frequency in rad/s
x0 = 0.1 # initial position in m
v0 = 0 # initial velocity in m/s
t_max = 10 # maximum time in s
dt = 0.01 # time step size in s
N = int(t_max/dt) # number of time steps

# Discretize the equation
x = np.zeros(N) # position array
v = np.zeros(N) # velocity array
t = np.linspace(0, t_max, N) # time array
x[0] = x0 # initial condition for position
v[0] = v0 # initial condition for velocity

# Solve the equation
for n in range(N-1):
    x[n+1] = x[n] + v[n]*dt # Euler method for position
    v[n+1] = v[n] - omega**2*x[n]*dt # Euler method for velocity

# Plot the solution
plt.plot(t, x, label="Position")
plt.plot(t, v, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Position (m) / Velocity (m/s)")
plt.title("Harmonic Oscillator")
plt.legend()
plt.show()
