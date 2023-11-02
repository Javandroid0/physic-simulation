from vpython import *

# Set up the scene
scene = canvas(title='Spring Oscillator', width=600, height=400)

# Define the parameters
m = 1.0  # mass of the object
k = 100.0  # spring constant
x0 = 0.5  # initial displacement
v0 = 0.0  # initial velocity

# Define the objects
spring = helix(pos=vector(0, 0, 0), axis=vector(0, -x0, 0), radius=0.1, coils=10, thickness=0.05)
mass = sphere(pos=vector(0, -x0, 0), radius=0.2, color=color.red)

# Define the initial conditions
mass.v = vector(0, v0, 0)
mass.p = mass.v * m

# Define the time step and total time
dt = 0.01
t = 0.0

# Define the loop for updating the position and velocity of the mass
while True:
    rate(100)
    F_spring = -k * (mass.pos - spring.pos)
    mass.p += F_spring * dt
    mass.v = mass.p / m
    mass.pos += mass.v * dt
    spring.axis = vector(0, -mass.pos.y, 0)
    t += dt
