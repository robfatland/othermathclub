


```
import turtle

from random import random
from turtle import Turtle
from math import sqrt
from math import cos
from math import sin
from math import atan2
from math import pi

def d(a, b): return sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def SetPlanets():
    global p, n, mass, radius, pSpace
    for i in range(n):
        if i == 0: p.append((0, 0, mass[i], radius[i]))   # place Jupiter at the origin
        else:                                             # four moons
            tryAgain = True
            while tryAgain:
                tryAgain = False
                xm, ym = -pSpace + 2*pSpace*random(), -pSpace + 2*pSpace*random()
                for j in range(i):
                    if d((xm, ym), (p[j][0], p[j][1])) < p[j][3] + radius[i]: tryAgain = True
            p.append((xm, ym, mass[i], radius[i]))

def DrawPlanets():
    for i in range(n): 
        s.up()
        s.setpos(p[i][0], p[i][1]-p[i][3])  # shift down by radius; with heading 0 places the center as desired
        s.down()
        s.circle(p[i][2]*rFactor)

s=Turtle(); s.speed(0); s.down(); s.dot(3); s.up()


# Acceleration multiplier: Determines how intense the gravity is
#   Make this negative for anti-gravity!!!
aFactor = 2.

pSpace = 160.
time = 300
subtime = 20
n = 5
mass = [10., 0.3, 4.1, 2.6, 3.3]
rFactor = 2
radius = [rFactor*i for i in mass]
p = []
SetPlanets()
DrawPlanets()
s.hideturtle()

b=Turtle(); b.speed(0); b.up(); b.color('red')
y0 = 20.
yI = 20.
ny = 4
for i in range(ny):
    x, y = -200., y0 + i*yI
    vx, vy = 0.5/float(subtime), 0.0/float(subtime)
    b.setpos(x,y)
    b.down()
    for t in range(time):
        for subt in range(subtime):
            for j in range(n):
                distance = d((x, y), (p[j][0],p[j][1]))
                accel = aFactor*p[j][2]/(distance*distance)/float(subtime)
                angle = pi*b.towards(p[j][0], p[j][1])/180.
                vx += accel*cos(angle)
                vy += accel*sin(angle)
            x = x + vx
            y = y + vy
        b.setheading((180./pi)*atan2(vy, vx))
        b.setpos(x, y)
        b.dot(1)
    b.up()       
```

