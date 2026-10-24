# AI in use: False
# trinket: [untested] | vscode: OK
#
# Project 6 — L-System
# Python Bytes / Curriculum
# Needs: Turtle, strings, the Chaos Game (same fractal, different method)
#
# Phase 1 (Rule S): grow a sentence of x/y/+/- by substitution.
# Phase 2 (Rule D): walk the finished sentence with a turtle to draw it.

from turtle import Turtle, done, tracer, update, Screen
screen = Screen()
screen.setup(width=700, height=700)

def CreateDirections(s, n):
  # Simon Says: return "+-+-+-+---++-"
  for i in range(n):
    s1 = ""
    for c in s:
      if c == "x":   s1 += "y+x+y"
      elif c == "y": s1 += "x-y-x"
      else:          s1 += c
    s = s1
  return s

go   =  9
n    =  6
bend = 60
d = CreateDirections("x", n)
print(d)

t = Turtle()
t.pencolor("blue"); t.setheading(60); t.penup()
if n % 2: t.goto(0, -300)
else: t.goto(-300, -300)
t.pendown()
tracer(0, 0)

for c in d:
  if c == "+":   t.left(bend);  t.forward(go)
  elif c == "-": t.right(bend); t.forward(go)

update()
done()