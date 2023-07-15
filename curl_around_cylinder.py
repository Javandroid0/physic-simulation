from mayavi import mlab
import numpy as np

# Define the surface function
def surface_func(u, v, radius, height):
    x = radius * np.cos(u)
    y = radius * np.sin(u)
    z = height * v
    return x, y, z

# Define the magnetic field components
def magnetic_field_components(u, v, radius, height, current):
    x = radius * np.cos(u)
    y = radius * np.sin(u)
    z = height * v
    Bx = -current * y / (2 * np.pi * radius**2)
    By = current * x / (2 * np.pi * radius**2)
    Bz = np.zeros_like(u)
    return Bx, By, Bz

# Generate the grid points
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(-1, 1, 30)
U, V = np.meshgrid(u, v)

# Set the radius and height of the cylinder
radius = 1.0
height = 2.0

# Set the current in the cylinder
current = 1.0

# Evaluate the surface function at grid points
X, Y, Z = surface_func(U, V, radius, height)

# Calculate the magnetic field components at each point
Bx, By, Bz = magnetic_field_components(U, V, radius, height, current)

# Create the Mayavi figure
fig = mlab.figure('Magnetic Field around Cylinder')

# Create the surface plot
surf = mlab.mesh(X, Y, Z, scalars=Z, colormap='viridis')

# Create arrows for the magnetic field
arrow_scale = 0.9
mlab.quiver3d(X, Y, Z, Bx, By, Bz, scale_factor=arrow_scale, color=(0, 0, 1))

# Set the view and show the plot
mlab.view(azimuth=45, elevation=30, distance=4)
mlab.show()
