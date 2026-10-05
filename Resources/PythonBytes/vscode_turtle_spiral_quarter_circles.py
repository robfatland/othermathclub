from turtle import Turtle, tracer, update

t = Turtle()


f = 3
df = 2             
alpha = 90

extent = 90

for s in range(70):
    t.circle(f, extent)
    f = f + df
    # t.left(alpha)
