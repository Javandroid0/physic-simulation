import matplotlib.pyplot as plt
import numpy as np

# Define the variables
E = -900 * 10 ** 14
m = 1000
M = 5.972 * 10 ** 24
G = 6.6743 * 10 ** (-11)
R = 6400000

# Define the function
def v(x):
    answer = np.sqrt(2/m * (E + G*M*m/x))
    print(x)
    print(answer)
    return answer

# Define the range of x values
x = np.linspace(1, 1000, 100000)

# Plot the function
plt.plot(x, v(x))

# Add labels and title
plt.xlabel('x')
plt.ylabel('v')
plt.title('Plot of v=sqrt(2/m * (E + GMm/x))')

# Show the plot
plt.show()
