import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Drawing")
screen.setup(width=800, height=600)

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)
spiral_turtle.color("cyan")
spiral_turtle.pensize(2)

def draw_spiral():
    for i in range(100):
        spiral_turtle.forward(i * 2)
        spiral_turtle.right(91)

draw_spiral()
screen.exitonclick()