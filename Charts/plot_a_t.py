# import numpy as np
# import matplotlib.pyplot as plt
#
# # Constants
# G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
# M = 5.972 * 10**24    # Mass of Earth in kg
# R = 6371000           # Radius of Earth in meters
# h = 1000              # Initial height in meters (for example, 1000 meters above Earth's surface)
#
# # Calculate gravitational acceleration at height h
# g = G * M / (R + h)**2
#
# # Time values from 0 to 100 seconds
# time = np.linspace(0, 100, 1000)  # 1000 points between 0 and 100 seconds
#
# # Calculate velocities at different times
# velocities = g * time
#
# # Plotting
# plt.figure(figsize=(8, 6))
# plt.plot(time, velocities, color='b', label='Velocity vs. Time')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Velocity (m/s)')
# plt.title(f'Velocity of Falling Object at {h} meters above Earth\'s Surface')
# plt.grid(True)
# plt.legend()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# # Constants
# G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
# M = 5.972 * 10**24    # Mass of Earth in kg
# R = 6371000           # Radius of Earth in meters
#
# # Heights from 1000 to 100000 meters (1 km to 100 km) with 100 points
# heights = np.linspace(1000, 100000, 100)  # 100 points from 1 km to 100 km
#
# # Calculate gravitational accelerations at different heights
# gravitational_accelerations = G * M / (R + heights)**2
#
# # Time values from 0 to 100 seconds
# time = np.linspace(0, 100, 1000)  # 1000 points between 0 and 100 seconds
#
# # Plotting velocities for different heights
# plt.figure(figsize=(8, 6))
# for i, h in enumerate(heights):
#     velocities = gravitational_accelerations[i] * time
#     plt.plot(time, velocities)
#
# plt.xlabel('Time (seconds)')
# plt.ylabel('Velocity (m/s)')
# plt.title('Velocity of Falling Object at Different Heights above Earth\'s Surface')
# plt.grid(True)
# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.674 * 10**-11  # Gravitational constant in m^3/kg/s^2
M = 5.972 * 10**24    # Mass of Earth in kg
R = 6371000           # Radius of Earth in meters

# Heights from 1000 to 100000 meters (1 km to 100 km) with 100 points
heights = np.linspace(1000, 100000, 100)  # 100 points from 1 km to 100 km

# Time values from 0 to 100 seconds
time = np.linspace(0, 100, 100)  # 100 points between 0 and 100 seconds

# Create a meshgrid of h and t values
H, T = np.meshgrid(heights, time)

# Calculate gravitational accelerations at different heights (negative sign)
gravitational_accelerations = -G * M / (R + H)**2

# Calculate velocities for different heights and times
velocities = gravitational_accelerations * T

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D surface
surf = ax.plot_surface(T,H, velocities, cmap='viridis')

# Labels and title
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Height (meters)')
ax.set_zlabel('Velocity (m/s)')
ax.set_title('Velocity of Falling Object as a Function of Height and Time')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
