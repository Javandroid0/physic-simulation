import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.6743e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24    # Mass of Earth (kg)
m = 1000         # Mass of object (kg)
E = -1           # Initial energy (J)

# Define initial conditions
x0 = 10000     # Initial distance from center of Earth (m)
v0 = 0           # Initial velocity (m/s)

# Define time range and step size
t0, tf = 0, 100000  # Start and end times (s)
dt = 1              # Time step size (s)

# Define function for dx/dt
def f(x, t):
    return np.sqrt(2/m) * np.sqrt(E + G*M*m/x)

# Define function for Runge-Kutta method
def rk4(x, t, dt):
    k1 = f(x, t)
    k2 = f(x + k1*dt/2, t + dt/2)
    k3 = f(x + k2*dt/2, t + dt/2)
    k4 = f(x + k3*dt, t + dt)
    return x + (k1 + 2*k2 + 2*k3 + k4)*dt/6

# Initialize arrays for x and t
x = np.zeros(int((tf-t0)/dt)+1)
t = np.zeros(int((tf-t0)/dt)+1)

# Set initial values
x[0] = x0
t[0] = t0

# Use Runge-Kutta method to solve for x(t)
for i in range(1, len(t)):
    x[i] = rk4(x[i-1], t[i-1], dt)
    t[i] = t[i-1] + dt

# Plot x(t)
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Distance from center of Earth (m)')
plt.title('Distance vs. Time')
plt.show()
