# import numpy as np
# from mayavi import mlab
#
# # Define the radius of the disk
# r = 1
#
# # Define the grid of points on the disk
# theta, phi = np.mgrid[0:2*np.pi:100j, 0:np.pi/2:100j]
# x = r*np.sin(phi)*np.cos(theta)
# y = r*np.sin(phi)*np.sin(theta)
# z = r*np.cos(phi)
#
# # Define the surface charge density function
# sigma = np.sin(phi)
#
# # Define the electric constant
# epsilon_0 = 8.85418782e-12
#
# # Calculate the electric field due to the surface charge density
# E_x = sigma/(2*epsilon_0)*np.sin(phi)*np.cos(theta)
# E_y = sigma/(2*epsilon_0)*np.sin(phi)*np.sin(theta)
# E_z = sigma/(2*epsilon_0)*np.cos(phi)
#
# # Plot the surface charge density and electric field on the disk
# mlab.quiver3d(x, y, z, E_x, E_y, E_z, scalars=sigma)
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
# # Define cylinder geometry
# r = 1
# h = 2
# theta = np.linspace(0, 2*np.pi, 100)
# z = np.linspace(-h/2, h/2, 100)
# theta, z = np.meshgrid(theta, z)
# print(theta)
# # Define electric field
# E = np.sin(theta) * np.exp(-z**20)
#
# # Create mesh grid for cylinder
# x = r * np.cos(theta)
# y = r * np.sin(theta)
#
# # Calculate electric field at each point on mesh grid
# Ex, Ey, Ez = E * x / r, E * y / r, E
#
# # Visualize electric field using Mayavi
# mlab.quiver3d(x, y, z, Ex, Ey, Ez)
# mlab.show()


# import math
# from mayavi import mlab
# from numpy import mgrid
#
# k = 9e9  # Coulomb's constant
# epsilon_0 = 8.85e-12  # permittivity of free space
# R = 1  # radius of disk
# sigma = 1  # volume charge density
# r = 2  # distance from center of disk to point where electric field is calculated
#
# E = (k * sigma * R ** 2) / (2 * epsilon_0 * math.sqrt(R ** 2 + r ** 2))
# print(f"The electric field at a distance {r} from the center of a disk with radius {R} and volume charge density {sigma} is {E:.2f} N/C.")
#
# # Create a meshgrid for the disk
# x, y = mgrid[-R:R:100j, -R:R:100j]
# z = x*0
#
# # Calculate the electric field for each point on the meshgrid
# Ex = (k * sigma * x) / (2 * epsilon_0 * (x**2 + y**2)**(3/2))
# Ey = (k * sigma * y) / (2 * epsilon_0 * (x**2 + y**2)**(3/2))
# Ez = z
#
# # Plot the electric field using Mayavi
# mlab.quiver3d(x, y, z, Ex, Ey, Ez, mode='arrow', scale_factor=1)
#
# # Add labels to the plot
# mlab.xlabel('X')
# mlab.ylabel('Y')
# mlab.zlabel('Z')
# mlab.title(f"Electric Field of a Disk with Radius {R} and Volume Charge Density {sigma}")
#
# # Display the plot
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 10.0  # Surface charge density (C/m^2)
# epsilon = 8.85e-12  # Electric permittivity of air (F/m)
#
# # Create data
# r, theta = np.mgrid[1:2:15j, 2:4*np.pi:50j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.ones_like(x) * 0.1
# print(x)
# A = np.pi * r[-1][-1]**2
# Q = sigma
# sigma_disk = Q / A
#
# # Calculate electric field vectors
# E_z = (sigma_disk / (2 * epsilon)) * (z / ((x**2 + y**2 + z**2)**(3/2)))
# E_x = - E_z * x / np.sqrt(x**2 + y**2)
# E_y = - E_z * y / np.sqrt(x**2 + y**2)
# #print(E_z)
# # Calculate surface charge density
#
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
# # Show plot
# mlab.show()


#
# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 10.0  # Surface charge density (C/m^2)
# #epsilon = 8.85e-12  # Electric permittivity of air (F/m)
# k = 8.99 * 10 **9
# # Create data
# r, theta = np.mgrid[1:2:15j, 2:4*np.pi:50j]
# x = r*np.cos(theta)
# y = r*np.cos(theta)
# z = np.ones_like(x)
# print(x)
# # A = np.pi * r[-1][-1]**2
# # Q = sigma
# # sigma_disk = Q / A
#
# # Calculate electric field vectors
# E_z = k * sigma *2 * np.log(np.exp())
# #E_x = - E_z * x / np.sqrt(x**2 + y**2)
# #E_y = - E_z * y / np.sqrt(x**2 + y**2)////(sigma_disk / (2 * epsilon)) * (z / ((x**2 + y**2 + z**2)**(3/2)))
# #print(E_z)
# # Calculate surface charge density
#
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z,  E_z)
#
# # Show plot
# mlab.show()
#

# import numpy as np
# from mayavi import mlab
#
# # Create data
# r, theta = np.mgrid[0:1:100j, 0:2*np.pi:100j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.zeros_like(x)
#
#
# # Plot data
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, )
# # Show plot
# mlab.show()

#
# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 1.0  # Surface charge density (C/m^2)
#
#
#
# # Create data
# r, theta = np.mgrid[0:1:100j, 2:4 * np.pi:100j]
# x = r * np.cos(theta)
# y = r * np.sin(theta)
# z = np.zeros_like(x)
#
#
# # Calculate electric field vectors
# # E_z = (sigma_disk / (2 * epsilon)) * (z / ((x ** 2 + y ** 2 + z ** 2) ** (3 / 2)))
# # E_x = - E_z * x / np.sqrt(x ** 2 + y ** 2)
# # E_y = - E_z * y / np.sqrt(x ** 2 + y ** 2)
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# #mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
# # Add coordinate system
# axes = mlab.axes()
# axes.axes.font_factor = 1.5
#
# # Show plot
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 1.0  # Surface charge density (C/m^2)
# k = 8.99e9  # Coulomb's constant (N⋅m^2/C^2)
# R = 0.5  # Radius of the disk (m)
# z = 1  # Distance from the center of the disk (m)
#
# # Create data
# r, theta = np.mgrid[0:R:20j, 0:2*np.pi:100j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.ones_like(x) * z
# #print(r)
#
# # Calculate electric field vectors
# E_z = 2 * k * np.pi * sigma * z * ((1 / z) - (1 / (z**2 + R**2)**0.5))
# E_x = np.zeros_like(x)
# E_y = np.zeros_like(y)
# print(z)
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(z, z, z, E_x, E_y, E_z)
#
# axes = mlab.axes()
# axes.axes.font_factor = 2
#
# # Show plot
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 1.0  # Surface charge density (C/m^2)
# epsilon = 8.85e-12  # Electric permittivity of air (F/m)
# k = 8.99e9  # Coulomb's constant (N⋅m^2/C^2)
# r = 0.5  # Radius of the disk (m)
# z = 0.1  # Distance from the center of the disk (m)
# q = -1e-6  # Point charge above the center of the disk (C)
# d = 0.05  # Distance between point charge and center of the disk (m)
#
# # Create data
# r, theta = np.mgrid[0:r:40j, 0:2*np.pi:100j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.ones_like(x) * z
#
# # Calculate electric field vectors
# E_z = 2 * k * np.pi * sigma * z * ((1 / z) - (1 / (z**2 + r**2)**0.5))
# E_x = np.zeros_like(x)
# E_y = np.zeros_like(x)
#
# # E_z_point_charge = k * q * (z - d) / ((x**2 + y**2 + (z - d)**2)**(3/2))
# # E_x_point_charge = k * q * x / ((x**2 + y**2 + (z - d)**2)**(3/2))
# # E_y_point_charge = k * q * y / ((x**2 + y**2 + (z - d)**2)**(3/2))
# #
# # E_x = E_x_disk + E_x_point_charge
# # E_y = E_y_disk + E_y_point_charge
# # E_z = E_z_disk + E_z_point_charge
#
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
#
# axes = mlab.axes()
# axes.axes.font_factor = 2
#
# # Show plot
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = 1.0  # Surface charge density (C/m^2)
# k = 8.99e9  # Coulomb's constant (N⋅m^2/C^2)
# r = 0.5  # Radius of the disk (m)
# z = 0.1  # Distance from the center of the disk (m)
#
# # Create data
# r, theta = np.mgrid[0:r:50j, 0:2*np.pi:100j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.ones_like(x) * z
#
# # Calculate electric field vectors
# E_z = 2 * k * np.pi * sigma * z * ((1 / z) - (1 / (z**2 + r**2)**0.5))
# E_x = np.zeros_like(x)
# E_y = np.zeros_like(x)
#
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
#
# axes = mlab.axes()
# axes.axes.font_factor = 2
#
# # Show plot
# mlab.show()
#

#
# import numpy as np
# from mayavi import mlab
#
# # Define constants
# sigma = -1.0  # Surface charge density (C/m^2)
# k = 8.99e9  # Coulomb's constant (N⋅m^2/C^2)
# r = 0.5  # Radius of the disk (m)
# z = 0.1  # Distance from the center of the disk (m)
#
# # Create data
# r, theta = np.mgrid[0:r:50j, 0:2*np.pi:100j]
# x = r*np.cos(theta)
# y = r*np.sin(theta)
# z = np.ones_like(x) * z
#
# # Calculate electric field vectors
# E_z = 2 * k * np.pi * sigma * z * ((1 / z) - (1 / (z**2 + r**2)**0.5))
# E_x = np.zeros_like(x)
# E_y = np.zeros_like(x)
#
# # Calculate vector from each point on the disk to the center of the disk
# vectors_x = -x
# vectors_y = -y
# vectors_z = -z
#
# # Normalize vectors
# norms = np.sqrt(vectors_x**2 + vectors_y**2 + vectors_z**2)
# vectors_x /= norms
# vectors_y /= norms
# vectors_z /= norms
#
# # Multiply normalized vectors by electric field magnitude to get final electric field vectors
# E_x *= vectors_x
# E_y *= vectors_y
# E_z *= vectors_z
#
# # Plot data and vectors
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
# axes = mlab.axes()
# axes.axes.font_factor = 2
#
# # Show plot
# mlab.show()


# import numpy as np
# from mayavi import mlab
#
#
# def electric_field_of_disk(R, d, sigma, x, y, z):
#     epsilon_0 = 8.854e-12  # Vacuum permittivity constant in F/m (farads per meter)
#     distance = np.sqrt(x ** 2 + y ** 2 + z ** 2)
#     if distance == 0:
#         return 0, 0, 0
#     if distance >= d:
#         cos_theta = z / distance
#         area = np.pi * R ** 2
#         dQ = sigma * area
#         E_magnitude = 1 / (4 * np.pi * epsilon_0) * dQ / distance ** 2
#         Ex = E_magnitude * cos_theta * x / distance
#         Ey = E_magnitude * cos_theta * y / distance
#         Ez = E_magnitude * cos_theta * z / distance
#         return Ex, Ey, Ez
#     else:
#         return 0, 0, 0
#
#
# # Define grid of points in 3D space
# x, y, z = np.mgrid[-5:5:20j, -5:5:20j, -5:5:20j]
#
# # Parameters of the charged disk
# R = 1.0  # Radius of the disk
# d = 2.0  # Distance from the point to the center of the disk
# sigma = 1.0  # Charge density of the disk in C/m^2
#
# # Calculate electric field at each point in the grid
# Ex, Ey, Ez = np.vectorize(electric_field_of_disk)(R, d, sigma, x, y, z)
#
# # Create a Mayavi vector field visualization
# fig = mlab.figure(size=(800, 600))
# mlab.quiver3d(x, y, z, Ex, Ey, Ez, scale_factor=0.001, color=(0.2, 0.4, 0.8))
#
# # Set visualization parameters
# mlab.axes()
# mlab.title('Electric Field of a Charged Disk')
# mlab.show()


# import math
#
# def electric_field(q, a, z):
#     k = 1 / (4 * math.pi * 8.8541878128e-12)
#     E_x = (k * q * z) / (2 * math.pi * a**2) * (1 / abs(z) - 1 / math.sqrt(z**2 + a**2))
#     E_y = (k * q * z) / (2 * math.pi * a**2) * (1 / abs(z) - 1 / math.sqrt(z**2 + a**2))
#     E_z = (k * q / (2 * math.pi * 8.8541878128e-12)) * ((z / abs(z)) / math.sqrt(z**2 + a**2))
#     return E_x, E_y, E_z
#
#


# import math
# import numpy as np
# from mayavi import mlab
#
# # Define constants
# q = 100.0  # Surface charge density (C/m^2)
# epsilon = 8.85e-12  # Electric permittivity of air (F/m)
# a = 50  # Radius of the disk (m)
# z = 10  # Distance from the center of the disk (m)
#
# # Create data
# r, theta = np.mgrid[0.001:a:10j, 0:2 * np.pi:100j]
# x = r * np.cos(theta)
# y = r * np.sin(theta)
# z = np.ones_like(x) * z
# a = r
# #print(z)
# k = 1 / (4 * math.pi * 8.8541878128e-12)
# E_x = (k * q * z) / (2 * math.pi * a ** 2) * (1 / np.abs(z) - 1 / np.sqrt(z ** 2 + a ** 2))
# E_y = (k * q * z) / (2 * math.pi * a ** 2) * (1 / np.abs(z) - 1 / np.sqrt(z ** 2 + a ** 2))
# E_z = (k * q / (2 * math.pi * 8.8541878128e-12)) * ((z / np.abs(z)) / np.sqrt(z ** 2 + a ** 2))
# # Plot data and vectors
# print(E_x)
# mlab.mesh(x, y, z)
# mlab.quiver3d(x, y, z, E_x, E_y, E_z)
#
# axes = mlab.axes()
# axes.axes.font_factor = 2
#
# # Show plot
# mlab.show()


import numpy as np
from mayavi import mlab


def midpoint_rule(func, a, b, num_intervals):
    interval_width = (b - a) / num_intervals
    integral_sum = 0
    for i in range(num_intervals):
        midpoint = a + (i + 0.5) * interval_width
        integral_sum += func(midpoint)
    return integral_sum * interval_width


def calculate_electric_field(x, y, z, a, sigma, num_intervals=1000):
    epsilon_0 = 8.854e-12  # Vacuum permittivity in F/m
    #theta_values = np.linspace(0, 2 * np.pi, num_intervals)

    # Define functions for electric field components
    def integrand_x(theta):
        return (x - a * np.cos(theta)) / ((x - a * np.cos(theta)) ** 2 + (y - a * np.sin(theta)) ** 2 + z ** 2)

    def integrand_y(theta):
        return (y - a * np.sin(theta)) / ((x - a * np.cos(theta)) ** 2 + (y - a * np.sin(theta)) ** 2 + z ** 2)

    def integrand_z(theta):
        return z / ((x - a * np.cos(theta)) ** 2 + (y - a * np.sin(theta)) ** 2 + z ** 2)

    # Calculate electric field components using midpoint rule
    E_x = (sigma * a / (2 * epsilon_0)) * midpoint_rule(integrand_x, 0, 2 * np.pi, num_intervals)
    E_y = (sigma * a / (2 * epsilon_0)) * midpoint_rule(integrand_y, 0, 2 * np.pi, num_intervals)
    E_z = (sigma * a / (2 * epsilon_0)) * midpoint_rule(integrand_z, 0, 2 * np.pi, num_intervals)
    print(E_z)
    return E_x, E_y, E_z


def plot_electric_field(a, sigma):
    # Calculate electric field components
    #E_x, E_y, E_z = calculate_electric_field(x, y, z, a, sigma, num_intervals)

    # Create a grid of points where the electric field will be plotted
    x_grid = np.linspace(-2 * a, 2 * a, 10)
    y_grid = np.linspace(-2 * a, 2 * a, 10)
    z_grid = np.linspace(-2 * a, 2 * a, 10)
    X, Y, Z = np.meshgrid(x_grid, y_grid, z_grid)

    # Calculate electric field at each point on the grid
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    Ez = np.zeros_like(Z)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            for k in range(X.shape[2]):
                Ex[i, j, k], Ey[i, j, k], Ez[i, j, k] = calculate_electric_field(X[i, j, k], Y[i, j, k], Z[i, j, k], a,
                                                                                 sigma)

    # Plot electric field using arrows
    mlab.quiver3d(X, Y, Z, Ex, Ey, Ez)

    # Plot disk using Mayavi's built-in functions
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi/2, 100)
    x_disk = a * np.outer(np.cos(u), np.sin(v))
    y_disk = a * np.outer(np.sin(u), np.sin(v))
    #z_disk = a * np.outer(np.ones(np.size(u)), np.cos(v))
    z_disk = np.ones_like(x_disk) - 1
    #print(z_disk)
    mlab.mesh(x_disk, y_disk, z_disk)

# Example usage
#x, y, z = 1, 1, 100  # Point where electric field is calculated
a = 5  # Radius of the charged disk
sigma = 1e-9  # Charge density in C/m^2 (1 nC/m^2)

plot_electric_field(a, sigma)
# axes = mlab.axes()
# axes.axes.font_factor = 2
mlab.show()
