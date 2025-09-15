# Same program as 'example.py' but fewer lines, some minor changes
import turtle
from turtle import Turtle

turtle.bgcolor(.95, .91, .85)    # conda Turtle uses floats from 0.0 to 1.0 for rgb values

s, s2, epsilon, close_distance, a_cumulative, nCycles = 390., 390./2., 0.2, 0.21, 0., 0.

def ni(i): return (i+1)%4   # ni is 'next index' in the square of bugs 0, 1, 2, 3

a = [] # a, b, c, d --> a[] we create a list of turtles to simplify the code
for i in range(4): a.append(Turtle()); a[i].up(); a[i].speed(1000)

b = Turtle()            # box > b
b.pencolor('black')

a[0].pencolor(1.0, 0.3, 0.3); a[1].pencolor(0.8, 0.9, 0.3); a[2].pencolor(0.3, 1.0, 0.3); a[3].pencolor(0.3, 0.8, 0.9)
a[0].setpos(-s2, s2); a[1].setpos(s2, s2); a[2].setpos(s2, -s2); a[3].setpos(-s2, -s2)
for i in range(4): a[i].down()

while True:
    for i in range(4): a[i].setheading(a[i].towards(a[ni(i)]))
    for i in range(4): a[i].forward(epsilon)
    if int(nCycles) % int(s/(6.*epsilon)) == 0:
        for i in range(4):
            b.up(); b.setpos(a[i].pos()); b.setheading(b.towards(a[ni(i)]));
            b.down(); b.forward(b.distance(a[ni(i)]))
    nCycles += 1.
    if a[0].distance(a[1]) < close_distance: break

print('Distance', "%.4f" % (nCycles * epsilon / s), 'in units of s')

