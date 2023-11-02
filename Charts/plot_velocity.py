import matplotlib.pyplot as plt
import numpy as np

# Define the variables
m = 10
E = -1
G = 6.6743e-11
M = 5.9722e24

# Define the function
def v(x):
    answer = np.sqrt(2/m * (E + G*M*m/x))
    # print(x)
    # print(answer)
    return answer

# Define the range of x values
x = np.linspace(1, 100, 1000)

# Plot the function
plt.plot(x, v(x))

# Add labels and title
plt.xlabel('x')
plt.ylabel('v')
plt.title('Plot of v=sqrt(2/m * (E + GMm/x))')

# Show the plot
plt.show()
