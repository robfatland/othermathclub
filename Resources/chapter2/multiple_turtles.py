# AI in use: True
# Chapter 2: Multiple turtles — Tier 3 drawing exercises
# trinket: [untested] | vscode: [untested]

from turtle import Turtle, Screen
from random import randint, choice


def turtle_race():
    """Two turtles race across the screen."""
    screen = Screen()
    screen.setup(600, 400)

    t1 = Turtle()
    t2 = Turtle()

    t1.penup()
    t2.penup()
    t1.goto(-250, 50)
    t2.goto(-250, -50)
    t1.pendown()
    t2.pendown()

    t1.pencolor("red")
    t2.pencolor("blue")
    t1.width(3)
    t2.width(3)

    t1.speed(0)
    t2.speed(0)

    for i in range(100):
        t1.forward(randint(1, 10))
        t2.forward(randint(1, 10))

    screen.mainloop()


def chase():
    """Turtle A chases turtle B (who wanders randomly)."""
    screen = Screen()
    screen.tracer(5, 0)

    runner = Turtle()
    chaser = Turtle()

    runner.pencolor("blue")
    chaser.pencolor("red")
    runner.penup()
    chaser.penup()
    runner.goto(100, 100)
    runner.pendown()
    chaser.pendown()

    for i in range(300):
        # Runner wanders
        runner.left(randint(-40, 40))
        runner.forward(8)

        # Chaser turns toward runner
        angle = chaser.towards(runner)
        chaser.setheading(angle)
        chaser.forward(6)

    screen.update()
    screen.mainloop()


def flock():
    """Five turtles, each doing its own random walk."""
    screen = Screen()
    screen.tracer(3, 0)

    colors = ["red", "blue", "green", "orange", "purple"]
    turtles = []
    for c in colors:
        t = Turtle()
        t.pencolor(c)
        t.speed(0)
        t.width(2)
        turtles.append(t)

    for i in range(200):
        for t in turtles:
            t.left(randint(-45, 45))
            t.forward(8)

    screen.update()
    screen.mainloop()


def chaos_game_preview():
    """
    Bridge to Chapter 3: The Chaos Game.
    Three fixed vertices. One turtle jumps halfway to a random vertex each step.
    What pattern emerges?
    """
    screen = Screen()
    screen.tracer(0, 0)

    # Three vertices of an equilateral-ish triangle
    vertices = [(-200, -150), (200, -150), (0, 200)]

    t = Turtle()
    t.penup()
    t.speed(0)
    t.hideturtle()

    # Start at a random vertex
    x, y = choice(vertices)
    t.goto(x, y)

    for i in range(10000):
        # Pick a random vertex
        vx, vy = choice(vertices)
        # Jump halfway there
        x = (x + vx) / 2
        y = (y + vy) / 2
        t.goto(x, y)
        t.dot(2, "black")

    screen.update()
    screen.mainloop()


# --- Uncomment one to run ---
# turtle_race()
# chase()
# flock()
# chaos_game_preview()
