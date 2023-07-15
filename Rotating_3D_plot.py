import numpy as np
import matplotlib.pyplot as plt


# Define the surface function
def surface_func(x, y):
    return x**2 + y**2


# Define the gradient function to calculate the normal vector
def gradient_func(x, y):
    dx = 2 * x
    dy = 2 * y
    dz = -1.0
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

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the vector field of normal vectors as blue arrows
arrow_scale = 0.2
ax.quiver(X, Y, Z, Nx, Ny, Nz, length=arrow_scale, color='blue')

# Set plot settings
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Field of Normals to a Surface (f(x, y) = x^2 + y^2)')

# Show the plot
plt.show()
