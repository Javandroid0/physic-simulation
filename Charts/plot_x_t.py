import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
M = 5.972 * 10**24    # Mass of Earth in kg
R = 6371000           # Radius of Earth in meters

# Initial height and initial velocity
h = 1000  # Initial height above the surface in meters
v_0 = 0   # Initial velocity in m/s (assuming the object starts from rest)

# Time values from 0 to 100 seconds
time = np.linspace(0, 100, 1000)  # 1000 points between 0 and 100 seconds

# Calculate positions for different times using the equation x(t) = h + v_0 t + (1/2) * (G * M / (R + h)^2) * t^2
positions = h + v_0 * time + 0.5 * (G * M / (R + h)**2) * time**2

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(time, positions, color='b', label='Position vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (meters)')
plt.title('Position of Falling Object as a Function of Time')
plt.grid(True)
plt.legend()
plt.show()
