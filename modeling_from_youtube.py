from vpython import *

k = 9e9  # N*m^2/C^2
Q = 2e-9
L = 0.05
xo = 0.05

N = 100
dQ = Q / N
dy = L / N

ro = vector(0.0, 0.04, 0)

# Make Rod
rq = vector(0, -L / 2 + dy / 2, 0)
charges = [sphere(pos=rq, radius=L / 40, color=color.cyan, q=dQ)]
# print("rq last = ",L/2-dy/2)
while rq.y < (L / 2):
    rq = rq + vector(0, dy, 0)
    charges = charges + [sphere(pos=rq, radius=L / 40, color=color.cyan, q=dQ)]


def E(rob, charges):
    Et = vector(0, 0, 0)
    for charge in charges:
        r = rob - charge.pos
        dE = k * charge.q * norm(r) / mag(r) ** 2
        Et = Et + dE
    return (Et)


Escale = 2e-7

stepx = 0.3 * L
stepy = 0.2 * L

theta = 0
dtheta = 2 * pi / 8

while theta < 2 * pi:
    ro = vector(stepx * cos(theta), -L, stepx * sin(theta))
    while ro.y < 1 * L:
        arrow(pos=ro, axis=Escale * E(ro, charges), color=color.yellow)
        ro = ro + vector(0, stepy, 0)

    ro = vector(2 * stepx * cos(theta), -L, 2 * stepx * sin(theta))
    while ro.y < 1 * L:
        arrow(pos=ro, axis=Escale * E(ro, charges), color=color.yellow)
        ro = ro + vector(0, stepy, 0)
    theta = theta + dtheta

