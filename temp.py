from vpython import *

f1 = gcurve(color=color.blue)
N = 15
g = vector(0,-9.8,0)
R = 0.2
Rr = R/10
h = 1
m = 0.05
k = 50
k2 = 1000 #spring constant with floor
ball = sphere(pos=vector(0,h/2,0),radius=R, opacity=0.4)
balls=[]
iballs=[] #these are the initial positions of the balls
theta=0
dtheta= 2*pi/N

floor = box(pos=vector(0,-h/2,0), size=vector(1,0.05,0.2))
while theta<2*pi:
  balls=balls+[sphere(pos=ball.pos+R*vector(cos(theta),sin(theta),0),radius=Rr, color=color.yellow)]
  theta=theta + dtheta
for i in range(len(balls)):
  iballs=iballs+[balls[i].pos]
for b in balls:
  b.m = m/N
  b.p = b.m*vector(0,0,0)
  b.F = b.m*g
#print(iballs)

t = 0
dt = 0.001

balls[0].p = balls[0].m*vector(0.,0,0)
rcom = vector(0,0,0)
for b in balls:
  rcom = rcom + b.pos*b.m
rcom =rcom/m
s0 = Rr+floor.size.y/2
while t<1.5:
  rate(500)
  rcom = vector(0,0,0)
  for b in balls:
    rcom = rcom + b.pos*b.m
  rcom =rcom/m
  ball.pos = rcom
  #go through each ball ball interaction.
  #calculate the L0 and then calculate the force
  for i in range(len(balls)):
    balls[i].F = balls[i].m*g
    for j in range(len(balls)):
      if i != j:
        #print("i = ",i," j = ",j)
        #find the orignial spring length
        L0 = mag(iballs[j]-iballs[i])
        L = balls[j].pos - balls[i].pos
        balls[i].F = balls[i].F - k*(L0 - mag(L))*norm(L)
  #check for floor collision
  for b in balls:
    s = b.pos.y-floor.pos.y
    if s<s0:
      b.F = b.F + k2*(s0-s)*vector(0,1,0)
  for b in balls:
    b.p = b.p + b.F*dt
    b.pos = b.pos + b.p*dt/b.m
  f1.plot(t,rcom.y)
  rcom = vector(0,0,0)
  for b in balls:
    rcom = rcom + b.pos*b.m
  rcom =rcom/m
  ball.pos = rcom

  t = t + dt