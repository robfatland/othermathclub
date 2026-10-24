# AI in use: True
# trinket: [untested] | vscode: [untested]
#
# Project 7 — Four Bugs
# Python Bytes / Curriculum
# Needs: Turtle, towards() / setheading() / distance(), while loop
#
# Four bugs sit at the corners of a square. Each one walks straight toward
# the next bug, over and over. Their targets keep moving, so they keep
# re-aiming. They spiral inward and meet at the center.
#
# Same three turtle methods as the Chaos Game:
#   a.towards(b)    — the angle from bug a to bug b
#   a.setheading(x) — point bug a that way
#   a.distance(b)   — how far apart they are (tells us when to stop)

from turtle import Turtle, Screen, tracer, update

screen = Screen()
screen.setup(width=600, height=600)
tracer(1, 0)            # refresh each move, but with no built-in delay

half = 250              # half the side of the square
side = 2 * half         # the full side length s
step = .25                # how far each bug walks per tick (bigger = faster)
done = step             # stop within one step, so a bigger step can't overshoot

# Four bugs, one per corner. Named for the physicists Alpher, Bethe, Gamow, Dyson.
a = Turtle(); a.pencolor("red")
b = Turtle(); b.pencolor("gold")
c = Turtle(); c.pencolor("green")
d = Turtle(); d.pencolor("blue")

for bug, (x, y) in zip((a, b, c, d), [(-half, half), (half, half), (half, -half), (-half, -half)]):
    bug.penup()
    bug.goto(x, y)
    bug.pendown()
    bug.speed(0)

# a chases b, b chases c, c chases d, d chases a.
# RE-AIM every bug first, THEN move them all one step. Lockstep matters.
ticks = 0
while a.distance(b) > done:
    a.setheading(a.towards(b))
    b.setheading(b.towards(c))
    c.setheading(c.towards(d))
    d.setheading(d.towards(a))
    a.forward(step)
    b.forward(step)
    c.forward(step)
    d.forward(step)
    ticks += 1

update()

# Each bug walked one step per tick, so total distance = ticks * step.
distance = ticks * step
print("Each bug walked", distance, "pixels.")
print("The table side is", side, "pixels.")
print("Distance / side =", round(distance / side, 4))

screen.mainloop()


# ----------------------------------------------------------------------
# Think on paper first (do NOT skip this)
# ----------------------------------------------------------------------
# Before coding: draw the square, step the bugs by hand a few times, and
# watch the shape shrink and twist toward the center.
#
# The punchline question: how FAR does each bug walk before they meet?
# (Surprising answer: exactly one side of the square. Measure and check.)
#
# Extensions:
#   - Try 3 bugs (triangle) or 6 bugs (hexagon). Change the corners.
#   - Make step bigger or smaller. Does the meeting point move?
