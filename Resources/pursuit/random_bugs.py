# AI in use: True  (header + bugfix added during consolidation; original logic by Rob)
# trinket: not tested | vscode: not tested
#
# Pursuit family — Random Bugs
# N turtles wander randomly, then all turn toward a common point (zero).
# Previously: Resources/4_Models/pursuit/randomturtles.py
#
# Fix applied during consolidation: the list was named `pens` but the loop
# referenced `pencolors[i]` (a NameError). Renamed references to `pens`.

from random import random, randint
from turtle import Turtle

pens = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'black']
zero = Turtle()
zero.hideturtle()
t = []
for i in range(7):
    t.append(Turtle())
    t[i].up()
    t[i].setpos(randint(-140, 140), randint(-140, 140))
    t[i].down()
    t[i].pencolor(pens[i])
    t[i].speed(1000)
    t[i].setheading(randint(-180, 180))

for acts in range(5):
    for i in range(100):
        for j in range(7):
            t[j].forward(randint(3, 6))
            t[j].setheading(t[j].heading() + randint(-35, 35))
    for i in range(40):
        for j in range(7):
            t[j].setheading(t[j].towards(zero))
            t[j].forward(5)
