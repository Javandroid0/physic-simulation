import matplotlib.pyplot as plt
import numpy as np

# Define the function v(x)
def v(x, R, M):
    g = 6.6743e-11 * M / R ** 2
    return np.sqrt(2 * g * R * (1 / R + x))

# Define the range of x values
x = np.linspace(-10, 100, 10000)

# Plot the function v(x)
plt.plot(x, v(x, 6.371e6, 5.972e24))

# Add a title and axis labels
plt.title("Velocity vs. Position")
plt.xlabel("Position (m)")
plt.ylabel("Velocity (m/s)")

# Display the plot
plt.show()
