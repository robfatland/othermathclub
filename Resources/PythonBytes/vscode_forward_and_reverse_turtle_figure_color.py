from turtle import Turtle
t = Turtle()
t.goto(-200, 0)
t.width(3)
x = 60
while x > 0:
    color_red = (255 - x/2)/256
    color_green = (255 - 2*x)/256
    color_blue = x/256
    t.pencolor(color_red, color_green, color_blue)
    t.forward(x*4)
    t.left(x)
    t.forward(10-x*3)
    x = x - 1

print('done!')
