print('I am the print() that escaped from handout 1!!')

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Intro - Python Bytes")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(3)          
t.pensize(3)        
t.color("blue")

t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)

s = input("tap enter")
# test me

t.penup()
t.goto(-150, -100)
t.pendown()
t.color("green")
t.circle(60)

s = input("tap enter")
# test me

t.penup()
t.goto(150, -100)
t.pendown()
t.dot(40, "orange")

s = input("tap enter")
# test me

t.penup()
t.goto(0, 0)
t.pendown()
t.color("magenta")
for step in range(60):
    t.forward(step * 4)
    t.right(91)

turtle.done()