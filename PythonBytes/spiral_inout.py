import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.pensize(2)

for i in range(200):
    distance = abs(math.sin(i * 0.1)) * 100
    t.forward(distance)
    t.right(91)

screen.exitonclick()