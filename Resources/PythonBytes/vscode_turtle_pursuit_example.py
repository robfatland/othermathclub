from time import time, sleep
from turtle import Turtle, tracer, update
from math import sqrt, cos

x0 = -300; y0 = -150; a0 = 20; a1 = 40.; step = 2; w = .015
u0 = -100; v0 =  350

def r_speed(s):
    if s < 39: return 4
    if s < 78: return 3
    return 2

q = Turtle(); r = Turtle()

# tracer(0, 0)

q.speed(0); q.up(); q.goto(x0, y0); q.down()
r.up(); r.goto(u0, v0); r.down(); r.pencolor("red")
for t in range(400):
    q.setheading(a0 + a1*cos(w*t)); q.forward(step)
    r2q = r.towards(q); r.setheading(r2q)
    rv = r_speed(r.distance(q))
    r.forward(rv)

# update()
