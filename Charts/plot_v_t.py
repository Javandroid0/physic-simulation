import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.6743e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24    # Mass of Earth (kg)
m = 100         # Mass of object (kg)
E = -1           # Initial energy (J)

# Define initial conditions
x0 = 6.371e6     # Initial distance from center of Earth (m)
v0 = 100           # Initial velocity (m/s)

# Define time range and step size
t0, tf = 0, 1000   # Start and end times (s)
dt = 1              # Time step size (s)

# Define function for dv/dt
def f(x, v):
    #print(x)
    return np.sqrt(2*m*G*(M+m)/x - 2*m*E/x**2)

# Define function for Runge-Kutta method
def rk4(v, t, dt):
    #print(x[0])
    k1 = f(x[0], v)
    k2 = f(x[0], v + k1*dt/2)
    k3 = f(x[0], v + k2*dt/2)
    k4 = f(x[0], v + k3*dt)
    return v + (k1 + 2*k2 + 2*k3 + k4)*dt/6

# Initialize arrays for x, v, and t
x = np.zeros(int((tf-t0)/dt)+1)
v = np.zeros(int((tf-t0)/dt)+1)
t = np.zeros(int((tf-t0)/dt)+1)

# Set initial values
x[0] = x0
v[0] = v0
t[0] = t0

# Use Runge-Kutta method to solve for v(t)
for i in range(1, len(t)):
    x[i] = rk4(v[i-1], t[i-1], dt)
    v[i] = rk4(v[i-1], t[i-1], dt)
    t[i] = t[i-1] + dt

# Plot v(t)
plt.plot(t, v)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time')
plt.show()
