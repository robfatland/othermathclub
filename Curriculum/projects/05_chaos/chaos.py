# AI in use: True
# trinket: [untested] | vscode: OK
#
# Project 5 — The Chaos Game
# Python Bytes / Curriculum
# Needs: Ms. Halfway (halfway + reset), Turtle, random.choice
#
# The idea (Egon's painting):
#   Three paint cans sit at the corners of a big triangle. Egon stands
#   somewhere, picks a corner at random, walks HALFWAY to it, and dabs a
#   dot. Then he picks another corner at random and does it again. Forever.
#
# This is Ms. Halfway again — but the destination is a random corner each step.
#
# Learning objective: aim and move the turtle with towards(), setheading(),
# and distance() instead of computing the midpoint by hand.

from random import choice, randint
from turtle import Turtle, Screen, tracer, update

screen = Screen()
screen.setup(width=700, height=700)
tracer(0, 0)            # draw fast: don't animate every dot

# The three corners (paint cans).
corners = [(-250, -200), (250, -200), (0, 250)]

t = Turtle()
t.hideturtle()
t.penup()

# Egon starts at a random spot OUTSIDE the triangle, off to one side. The first
# few jumps leave stray dots as he gets pulled onto the pattern — watch for them.
t.goto(randint(300, 340), randint(-50, 50))

# DOT_SIZE is the whole ballgame. Too big and the dots merge into a solid
# triangle. Too small and it looks like dust. Try 2, then try 6, then try 1.
DOT_SIZE = 2

for step in range(20000):
    target = choice(corners)        # pick a random corner
    t.setheading(t.towards(target)) # aim straight at it
    half = t.distance(target) / 2   # how far is halfway?
    t.forward(half)                 # walk halfway and stop
    t.dot(DOT_SIZE, "red")          # dab a dot right here

update()
screen.mainloop()


# ----------------------------------------------------------------------
# Predict first, then run (do NOT skip this)
# ----------------------------------------------------------------------
# A totally random process. What could the picture possibly be? Have the
# student commit to a guess before running. The answer is a surprise: the
# dots do NOT fill the triangle. A fractal appears — the Sierpinski gasket.
#
# Extensions:
#   - Change DOT_SIZE. Watch the structure appear and disappear.
#   - 4 corners instead of 3 (a square). Does a fractal appear? (Try it.)
#   - Walk a different fraction, not 1/2. Try 1/3, 2/3. Try past 1. Try
#     a negative fraction. What happens for a jump in [0, 1]? Above 1? Below 0?
