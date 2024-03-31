import numpy as np
from mayavi import mlab

# Define the grid of points in space
x, y, z = np.mgrid[-5:6, -5:6, -5:6]

# Define the charges and their positions
q = 1.0
rod_length = 9
rod_charges = [(q, (i, 0, 0)) for i in range(-rod_length//2+1, rod_length//2+1)]

# Calculate the electric field at each point in space
Ex, Ey, Ez = np.zeros_like(x).astype('float64'), np.zeros_like(y).astype('float64'), np.zeros_like(z).astype('float64')
for charge in rod_charges:
    r = np.sqrt((x - charge[1][0]) ** 2 + (y - charge[1][1]) ** 2 + (z - charge[1][2]) ** 2)
    Ex += charge[0] * (x - charge[1][0]) / r ** 3
    Ey += charge[0] * (y - charge[1][1]) / r ** 3
    Ez += charge[0] * (z - charge[1][2]) / r ** 3
# Plot the electric field using Mayavi
mlab.quiver3d(x, y, z, Ex, Ey, Ez)
mlab.points3d([charge[1][0] for charge in rod_charges], [charge[1][1] for charge in rod_charges], [charge[1][2] for charge in rod_charges], scale_factor=1.5*q)
mlab.show()
