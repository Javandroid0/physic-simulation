import numpy as np
from mayavi import mlab

# Define the grid of points in space
x, y, z = np.mgrid[-2:3, -2:3, -2:3]

# Define the charge and its position
q = 1.0
x0, y0, z0 = 0, 0, 0

# Calculate the electric field at each point in space
r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2)
Ex = q * (x - x0) / r ** 3
Ey = q * (y - y0) / r ** 3
Ez = q * (z - z0) / r ** 3

# Plot the electric field using Mayavi
mlab.quiver3d(x, y, z, Ex, Ey, Ez)
mlab.show()
