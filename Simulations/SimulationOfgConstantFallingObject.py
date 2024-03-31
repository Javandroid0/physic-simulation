from vpython import *

# Set up the scene
scene = canvas(title='Falling Ball', width=600, height=400)
floor = box(pos=vector(0, -5, 0), size=vector(10, 0.2, 10), color=color.blue)

# Set up the ball
ball = sphere(pos=vector(0, 10, 0), radius=1, color=color.red)
ball.velocity = vector(0, -9.8, 0)  # Initial velocity


# Animate the ball
dt = 0.01
while ball.pos.y > floor.pos.y + floor.size.y / 2 + ball.radius:
    rate(100)
    ball.pos += ball.velocity * dt
    ball.velocity += vector(0, -9.8, 0) * dt
    print(ball.velocity)
# Print final position of the ball
print(f"The final position of the ball is {ball.pos}.")
