import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
M = 5.972 * 10**24    # Mass of Earth in kg
R = 6371000           # Radius of Earth in meters

# Heights from 1000 to 100000 meters (1 km to 100 km) with 100 points
heights = np.linspace(1000, 100000, 100)  # 100 points from 1 km to 100 km

# Time values from 0 to 100 seconds with 100 points
time = np.linspace(0, 100, 100)  # 100 points between 0 and 100 seconds

# Create a meshgrid of h and t values
H, T = np.meshgrid(heights, time)

# Calculate positions for different heights and times using the equation x(h, t) = h + 0.5 * (G * M / (R + h)^2) * t^2
positions = H + 0.5 * (G * M / (R + H)**2) * T**2

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D surface
surf = ax.plot_surface(H, T, positions, cmap='viridis')

# Labels and title
ax.set_xlabel('Height (meters)')
ax.set_ylabel('Time (seconds)')
ax.set_zlabel('Position (meters)')
ax.set_title('Position of Falling Object as a Function of Height and Time')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
