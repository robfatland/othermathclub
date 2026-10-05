from turtle import Turtle, tracer, update
from random import choice, randint

tracer(0, 0)

t = Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta', 'lime', 'pink']

n_spirals = 20

for spiral in range(n_spirals):
    t.penup()
    t.goto(randint(-200, 200), randint(-200, 200))
    t.pendown()
    t.color(choice(colors))
    t_go = randint(0, 20)
    t_dot = randint(2, 10)
    t_turn = randint(-100, 100)
    t_increment = randint(1, 6)
    t_steps = randint(30, 160)

    for _ in range(t_steps):
        t.forward(t_go)
        t.dot(t_dot)
        t.right(t_turn)
        t_go += t_increment

update()
