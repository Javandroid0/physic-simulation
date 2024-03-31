# from math import sqrt
#
# from vpython import *
#
# m = 1e3  # mass of the falling ball in kg
# E = 0  # energy of the falling ball in J
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24  # mass of the Earth in kg
#
#
# def f_g(x):
#     return (G * M * m) / x
#
#
# def f_v(x):
#     return sqrt(2 / m * (E + f_g(x)))
#
#
# scene = canvas(title='Falling Ball', width=600, height=400)
# floor = box(pos=vector(0, f_v(2), 0), size=vector(10, 0.2, 10), color=color.blue)
#
# ball = sphere(pos=vector(0, f_v(2), 0), radius=1, color=color.red)
#
# ball.velocity = vector(0, f_v(2), 0)
#
# dt = 0.01
# while ball.pos.y > floor.pos.y + floor.size.y / 2 + ball.radius:
#     rate(100)
#     ball.pos += ball.velocity * dt
#     ball.velocity += vector(0, -9.8, 0) * dt * f_v(2)
#     print(ball.velocity)
# # v=dx/dt=sqrt(2/m * (E + GMm/x))

# import vpython as vp
#
# # Create a ball representing the Earth
# earth = vp.sphere(pos=vp.vector(0, 0, 0), radius=6.371e6, color=vp.color.blue)
#
# # Create another ball as a falling object
# falling_ball = vp.sphere(pos=vp.vector(0, 1e7, 0), radius=1e5, color=vp.color.red)
#
# # Set the initial velocity of the falling ball using the given formula
# m = 1000  # mass of the falling ball in kg
# E = 4 * 10 ** 11  # energy of the falling ball in J
# G = 6.6743e-11  # gravitational constant in m^3/kg/s^2
# M = 5.9722e24  # mass of the Earth in kg
# x = falling_ball.pos - earth.pos  # vector from center of Earth to position of falling ball
# v = vp.sqrt(2 / m * (E + G * M * m / vp.mag(x))) * vp.norm(
#     vp.cross(x, vp.vector(0, 0, 1)))  # velocity of the falling ball in m/s
# falling_ball.velocity = v
#
# # Set up the animation loop
# dt = 1e-2  # time step in seconds
# t = 0  # current time in seconds
# while True:
#     vp.rate(100)  # maximum number of iterations per second
#     t += dt  # update current time
#     falling_ball.pos += falling_ball.velocity * dt  # update position of the falling ball
#     x = falling_ball.pos - earth.pos  # update vector from center of Earth to position of falling ball
#     # print(x)
#     a = (-G * M * x / vp.mag(x) ** 3)  # acceleration of the falling ball due to gravity
#     falling_ball.velocity += a * dt  # update velocity of the falling ball due to gravity
#     print(falling_ball.velocity)
#     if vp.mag(falling_ball.pos) < earth.radius:  # check if the falling ball has hit the ground
#         break
#
# print("The falling ball hit the ground after", t, "seconds.")

# 1/(sqrt(-6*10^10+(6 * 10^16 * 6.7)/(x + 6400000) )) x=10000 to 0


import numpy as np
from threading import Thread
from vpython import *

# Create a ball representing the Earth
earth = sphere(pos=vector(0, 0, 0), radius=6.371e6, color=color.blue)

# Create another ball as a falling object
falling_ball = sphere(pos=vector(0, 1e7, 0), radius=1e5, color=color.red)

# Set the initial velocity of the falling ball using the given formula
m = 1e3 # mass of the falling ball in kg
E = 0 # energy of the falling ball in J
G = 6.6743e-11 # gravitational constant in m^3/kg/s^2
M = 5.9722e24 # mass of the Earth in kg
x = mag(falling_ball.pos) # distance between the center of the Earth and the falling ball in m
v = sqrt(2/m * (E + G*M*m/x)) * norm(cross(falling_ball.pos, vector(0, 0, 1))) # velocity of the falling ball in m/s
falling_ball.velocity = v

def animate():
    # Set up the animation loop
    dt = 1e-2 # time step in seconds
    t = 0 # current time in seconds
    while True:
        rate(100) # maximum number of iterations per second
        t += dt # update current time
        falling_ball.pos += falling_ball.velocity * dt # update position of the falling ball
        x = mag(falling_ball.pos) # update distance between the center of the Earth and the falling ball
        a = -G*M*x/mag(x)**3 * falling_ball.pos # acceleration of the falling ball due to gravity
        falling_ball.velocity += a * dt  # update velocity of the falling ball due to gravity
        if mag(falling_ball.pos) < earth.radius: # check if the falling ball has hit the ground
            break

    print("The falling ball hit the ground after", t, "seconds.")

if __name__ == '__main__':
    # Register an atexit function to stop VPython's event loop when Python exits
    atexit.register(lambda: vpython_control.stop())

    # Create a VPython canvas and start its event loop in a separate thread
    vpython_control = canvas(background=color.white)
    Thread(target=vpython_control.mainloop).start()

    # Create VPython objects on the canvas and start animating them in a separate thread
    Thread(target=animate).start()


# import numpy as np
# from scipy.integrate import odeint
#
#
# # Define the function to integrate
# def f(y, x, E, m, M, G, R):
#     return 1 / np.sqrt(E + (m * M * G) / (x + R))
#
#
# # Define the parameters
# E = -6 * 10 ** 10
# m = 1000
# M = 5.972 * 10 ** 24
# G = 6.6743 * 10 ** (-11)
# R = 6400000
#
# # Define the initial conditions
# y0 = 0
#
# # Define the x values to integrate over
# x = np.linspace(0, 10000, 100000)
#
# # Use the Runge-Kutta method to solve the integral
# result = odeint(f, y0, x, args=(E, m, M, G, R))
#
# # Print the result of the integral
# print("The result of the integral is:", result[-1])
