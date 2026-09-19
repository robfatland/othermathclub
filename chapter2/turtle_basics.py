# AI in use: True
# Chapter 2: Turtle basics — first drawing exercises
# trinket: [untested] | vscode: [untested]

from turtle import Turtle, Screen


def square():
    """Draw a square."""
    t = Turtle()
    for i in range(4):
        t.forward(100)
        t.left(90)
    Screen().mainloop()


def polygon(sides, size):
    """Draw a regular polygon with the given number of sides."""
    t = Turtle()
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)
    Screen().mainloop()


def spiral():
    """Draw a spiral — forward distance grows each step."""
    t = Turtle()
    t.speed(0)
    for i in range(100):
        t.forward(i * 2)
        t.left(91)
    Screen().mainloop()


def star():
    """Draw a 5-pointed star."""
    t = Turtle()
    t.pencolor("gold")
    t.width(3)
    for i in range(5):
        t.forward(150)
        t.left(144)
    Screen().mainloop()


# --- Uncomment one to run ---
# square()
# polygon(6, 80)
# spiral()
# star()
