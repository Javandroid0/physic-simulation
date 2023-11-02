import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
M = 5.972 * 10**24    # Mass of Earth in kg
R = 6371000           # Radius of Earth in meters

# Heights from 1000 to 100000 meters (1 km to 100 km) with 100 points
heights = np.linspace(1000, 100000, 100)  # 100 points from 1 km to 100 km

# Calculate gravitational accelerations at different heights (negative sign)
gravitational_accelerations = G * M / (R + heights)**2

# Time (assuming a specific value, e.g., 10 seconds)
time = 10  # seconds

# Calculate velocities for different heights at the specified time
velocities = gravitational_accelerations * time

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(heights, velocities, color='b', label=f'Velocity at {time} seconds')
plt.xlabel('Height (meters)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity of Falling Object as a Function of Height')
plt.grid(True)
plt.legend()
plt.show()
