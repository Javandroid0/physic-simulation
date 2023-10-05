import numpy as np
from mayavi import mlab

# Define the cylinder's dimensions
radius = 1
height = 20

# Define the electric constant
epsilon_0 = 8.85418782e-12

# Define the surface charge density
sigma = 1e-6

# Create the cylinder using Numpy
theta = np.linspace(0, 2 * np.pi, 20)
z = np.linspace(0, height, 10)
theta_grid, z_grid = np.meshgrid(theta, z)
x_grid = radius * np.cos(theta_grid)
y_grid = radius * np.sin(theta_grid)

# Calculate the electric field of every plate
E = sigma / (2 * epsilon_0)

# Visualize the cylinder and electric field using Mayavi
fig = mlab.figure(bgcolor=(1, 1, 1), size=(400, 400))
mlab.mesh(x_grid, y_grid, z_grid, colormap='Blues')
mlab.quiver3d(x_grid.reshape(-1), y_grid.reshape(-1), z_grid.reshape(-1), E * np.cos(theta_grid).reshape(-1), E * np.sin(theta_grid).reshape(-1), np.zeros_like(z_grid).reshape(-1))
mlab.show()
