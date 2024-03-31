import numpy as np
from mayavi import mlab


# Define the surface function
def surface_func(x, y):
    return np.sin(x) * np.cos(y)


# Define the gradient function to calculate the normal vector
def gradient_func(x, y):
    dx = np.cos(x) * np.cos(y)
    dy = -np.sin(x) * np.sin(y)
    dz = 1.0
    magnitude = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    return dx / magnitude, dy / magnitude, dz / magnitude


# Generate the grid points
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Evaluate the surface function at grid points
Z = surface_func(X, Y)

# Calculate the unit normal vectors at each point
Nx, Ny, Nz = gradient_func(X, Y)

# Create a figure
fig = mlab.figure('Vector Field of Normals', bgcolor=(1, 1, 1))

# Create the surface plot
surface = mlab.mesh(X, Y, Z, color=(0.8, 0.8, 0.8))

# Create arrows for the vector field of normal vectors
arrow_scale = 0.3
mlab.quiver3d(X, Y, Z, Nx, Ny, Nz, scale_factor=arrow_scale, color=(0, 0, 1))

# Run the visualization
mlab.show()
