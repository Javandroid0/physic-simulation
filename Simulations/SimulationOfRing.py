import numpy as np
from mayavi import mlab

# Define the charge location and magnitude
theta = np.linspace(0, 2 * np.pi, 100)
x, y, z = np.cos(theta), np.sin(theta), np.zeros_like(theta)
q = np.ones_like(theta)

# Create the electric field vectors
Ex, Ey, Ez = q * x, q * y, q * z

# Plot the electric field vectors and ring of charges
mlab.quiver3d(x, y, z, Ex, Ey, Ez)
mlab.plot3d(x, y, z)
mlab.show()
