import matplotlib.pyplot as plt
import numpy as np

G = 6.67430e-11  # gravitational constant
M = 5.972e24     # mass of Earth in kg
R = 6371000      # radius of Earth in meters

def g(h):
    return G * M / (R + h)**2

h = np.linspace(0, 60009999)
plt.plot(h, g(h))
plt.xlabel('Height (m)')
plt.ylabel('g (m/s^2)')
plt.title('Gravitational acceleration vs height')
plt.show()
