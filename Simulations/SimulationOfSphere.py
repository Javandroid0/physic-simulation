from mayavi import mlab
import numpy as np

# Define the surface function
def surface_func(theta, phi, r):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# Define the gradient function to calculate the normal vector
# def gradient_func(theta, phi, r):
#     dx = np.sin(theta) * np.cos(phi)
#     dy = np.sin(theta) * np.sin(phi)
#     dz = np.cos(theta)
#     magnitude = np.sqrt(dx**2 + dy**2 + dz**2)
#     nx = dx / magnitude
#     ny = dy / magnitude
#     nz = dz / magnitude
#     return nx, ny, nz
#
# Generate the grid points
theta, phi = np.mgrid[0:np.pi:30j, 0:np.pi:30j]

# Set the radius of the sphere
radius = 1.0

# Evaluate the surface function at grid points
X, Y, Z = surface_func(theta, phi, radius)

# Calculate the unit normal vectors at each point
#Nx, Ny, Nz = gradient_func(theta, phi, radius)

# Create the Mayavi figure
fig = mlab.figure('Vector Field of Normals')

# Create the surface plot
surf = mlab.mesh(X, Y, Z, scalars=Z, colormap='viridis')

# Create arrows for the vector field of normal vectors
arrow_scale = 0.1
#mlab.quiver3d(X, Y, Z, Nx, Ny, Nz, scale_factor=arrow_scale, color=(0, 0, 1))

# Set the view and show the plot
mlab.view(azimuth=45, elevation=30, distance=4)
mlab.show()
