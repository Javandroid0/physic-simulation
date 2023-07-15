from mayavi import mlab
import numpy as np

# Define the surface function
def surface_func(u, v, radius, height):
    x = radius * np.cos(u)
    y = radius * np.sin(u)
    z = height * v
    return x, y, z

# Define the gradient function to calculate the normal vector
def gradient_func(u, v, radius, height):
    dx = radius * np.cos(u)
    dy = radius * np.sin(u)
    dz = np.zeros_like(u)
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2)
    nx = dx / magnitude
    ny = dy / magnitude
    nz = dz / magnitude
    return nx, ny, nz

# Generate the grid points
u = np.linspace(0, 2*np.pi, 30)
v = np.linspace(-1, 1, 30)
U, V = np.meshgrid(u, v)

# Set the radius and height of the cylinder
radius = 1.0
height = 2.0

# Evaluate the surface function at grid points
X, Y, Z = surface_func(U, V, radius, height)

# Calculate the unit normal vectors at each point
Nx, Ny, Nz = gradient_func(U, V, radius, height)

# Create the Mayavi figure
fig = mlab.figure('Vector Field of Normals')

# Create the surface plot
surf = mlab.mesh(X, Y, Z, scalars=Z, colormap='viridis')

# Create arrows for the vector field of normal vectors
arrow_scale = 0.1
mlab.quiver3d(X, Y, Z, Nx, Ny, Nz, scale_factor=arrow_scale, color=(0, 0, 1))

# Set the view and show the plot
mlab.view(azimuth=45, elevation=30, distance=4)
mlab.show()
