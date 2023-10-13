import numpy as np
import matplotlib.pyplot as plt

k = 9e9  # N*m^2/C^2
Q = 2e-9
L = 0.05

N = 100
dQ = Q / N
dy = L / N

y = np.linspace(-L / 2, L / 2, N)
E = np.zeros_like(y)

for i in range(N):
    for j in range(N):
        r = np.sqrt(y[i] ** 2 + y[j] ** 2)
        E[i] += k * dQ * y[j] / r ** 3

plt.plot(y, E)
plt.xlabel('y (m)')
plt.ylabel('Electric field (N/C)')
plt.title('Electric field of a charged rod')
plt.show()
