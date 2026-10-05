# AI in use: True
# trinket: OK | vscode: OK
#
# Project 1 — Ms. Halfway
# Python Bytes / Curriculum
# Needs: Syntax 1 (variables, average function)
#
# Premise (do this on paper first):
#   Ms. Halfway stands at a spot x. She wants to reach a destination d.
#   But she only ever walks to the point halfway between where she is and
#   where she wants to go. That halfway point is p = average(x, d).
#   Then she "resets": she is now standing at p. Repeat.
#   Where does she end up after ten steps?
#
# Variables:
#   x = where she is
#   d = where she wants to go
#   p = where she pauses (the halfway point)

# average is defined INLINE here so this project stands on its own.
# (It is the same recipe built in Syntax 1.)
def average(first, second):
    return (first + second) / 2

# Starting conditions
x = 0
d = 1
p = average(x, d)       # the first halfway point: 0.5

# One step is: compute the halfway point, then RESET so she stands there.
# "Reset" is the heart of this project: x becomes p.
#
# We repeat that step ten times.
for step in range(10):
    p = average(x, d)   # where she pauses this time
    x = p               # the reset: she is now standing at the pause point

print(x)                # how close did she get to d = 1 after ten halvings?


# ----------------------------------------------------------------------
# Where this is going (do NOT rush to it)
# ----------------------------------------------------------------------
# - What is x after 10 steps? After 20? Does it ever exactly reach d?
# - Try other destinations: d = 7, d = 100. Try starting x somewhere else.
# - Later: what if, each step, d is chosen at random from a few fixed points?
#   That small change is the doorway to the Chaos Game.
