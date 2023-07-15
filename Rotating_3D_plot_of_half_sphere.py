from mayavi import mlab
import numpy as np

# Define the surface function
def surface_func(x, y, r):
    mask = x**2 + y**2 <= r**2
    z = np.zeros_like(x)
    z[mask] = np.sqrt(r**2 - x[mask]**2 - y[mask]**2)
    return z

# Define the gradient function to calculate the normal vector
def gradient_func(x, y, r):
    mask = x**2 + y**2 <= r**2
    dx = -x[mask]
    dy = -y[mask]
    dz = np.sqrt(1 - x[mask]**2 - y[mask]**2)
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2)
    nx = np.zeros_like(x)
    ny = np.zeros_like(y)
    nz = np.zeros_like(x)
    nx[mask] = dx / magnitude
    ny[mask] = dy / magnitude
    nz[mask] = dz / magnitude
    return nx, ny, nz

# Generate the grid points
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Set the radius of the sphere
radius = 1.0

# Evaluate the surface function at grid points
Z = surface_func(X, Y, radius)

# Calculate the unit normal vectors at each point
Nx, Ny, Nz = gradient_func(X, Y, radius)

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
