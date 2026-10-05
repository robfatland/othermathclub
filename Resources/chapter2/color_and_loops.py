# AI in use: True
# Chapter 2: Color and loops — Tier 2 drawing exercises
# trinket: [untested] | vscode: [untested]

from turtle import Turtle, Screen


def rainbow_spiral():
    """Spiral that changes color each step."""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t = Turtle()
    t.speed(0)
    t.width(2)
    for i in range(60):
        t.pencolor(colors[i % len(colors)])
        t.forward(i * 3)
        t.left(61)
    Screen().mainloop()


def concentric_squares():
    """Draw concentric squares with different colors."""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    screen = Screen()
    screen.tracer(0, 0)
    t = Turtle()
    t.width(2)
    t.penup()
    for k in range(6):
        size = 50 + k * 30
        t.goto(-size / 2, -size / 2)
        t.pendown()
        t.pencolor(colors[k])
        for i in range(4):
            t.forward(size)
            t.left(90)
        t.penup()
    screen.update()
    screen.mainloop()


def dot_grid():
    """Draw a grid of dots using nested loops."""
    screen = Screen()
    screen.tracer(0, 0)
    t = Turtle()
    t.penup()
    colors = ["red", "blue", "green", "orange", "purple"]
    for row in range(10):
        for col in range(10):
            x = -200 + col * 40
            y = 200 - row * 40
            t.goto(x, y)
            t.dot(15, colors[(row + col) % len(colors)])
    screen.update()
    screen.mainloop()


def random_walk():
    """Random walk: random angle, fixed step, 200 iterations."""
    from random import randint
    t = Turtle()
    t.speed(0)
    t.width(1)
    for i in range(200):
        t.left(randint(-90, 90))
        t.forward(10)
    Screen().mainloop()


# --- Uncomment one to run ---
# rainbow_spiral()
# concentric_squares()
# dot_grid()
# random_walk()
