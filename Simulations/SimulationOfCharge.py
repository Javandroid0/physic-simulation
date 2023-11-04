import numpy as np
from mayavi import mlab

# Define the grid
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(-2, 2, 10)

# Create the grid
x, y, z = np.meshgrid(x, y, z)
# Define the charges
q1 = 100
q2 = -5
print(x)
# Define the electric field
k = 9e9  # Coulomb's constant
r1 = np.sqrt((x - 1) ** 2 + y ** 2 + z ** 2)
r2 = np.sqrt((x + 1) ** 2 + y ** 2 + z ** 2)
denom1 = r1 ** 3
denom2 = r2 ** 3
E_x = k * q1 * np.where(denom1 == 0, 0, (x - 1) / denom1) + k * q2 * np.where(denom2 == 0, 0, (x + 1) / denom2)
E_y = k * q1 * np.where(denom1 == 0, 0, y / denom1) + k * q2 * np.where(denom2 == 0, 0, y / denom2)
E_z = k * q1 * np.where(denom1 == 0, 0, z / denom1) + k * q2 * np.where(denom2 == 0, 0, z / denom2)

# Define the charge positions
charge_pos_1 = np.array([1, 0, 0])
charge_pos_2 = np.array([-1, 0, 0])

# Plot the electric field lines and charges
mlab.quiver3d(x, y, z, E_x, E_y, E_z)
mlab.points3d(charge_pos_1[0], charge_pos_1[1], charge_pos_1[2], color=(1, 0, 0), scale_factor=0.2)
mlab.points3d(charge_pos_2[0], charge_pos_2[1], charge_pos_2[2], color=(0, 0, 1), scale_factor=0.2)

# axes = mlab.axes()
# axes.axes.font_factor = 2

mlab.show()
