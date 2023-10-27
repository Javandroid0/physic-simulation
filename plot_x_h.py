import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
M = 5.972 * 10**24    # Mass of Earth in kg
R = 6371000           # Radius of Earth in meters

# Time (assuming a specific value, e.g., 10 seconds)
t = 10  # seconds

# Heights from 1000 to 100000 meters (1 km to 100 km) with 100 points
heights = np.linspace(1000, 100000, 100)  # 100 points from 1 km to 100 km

# Calculate positions for different heights using the equation x(h) = h + 0.5 * (G * M / (R + h)^2) * t^2
positions = heights + 0.5 * (G * M / (R + heights)**2) * t**2

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(heights, positions, color='b', label=f'Position at t={t} seconds')
plt.xlabel('Height (meters)')
plt.ylabel('Position (meters)')
plt.title('Position of Falling Object as a Function of Height')
plt.grid(True)
plt.legend()
plt.show()
