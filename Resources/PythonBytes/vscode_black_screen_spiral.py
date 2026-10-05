import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Drawing")
screen.setup(width=800, height=600)

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest speed
spiral_turtle.color("cyan")
spiral_turtle.pensize(2)

# Draw the spiral
def draw_spiral():
    for i in range(100):
        spiral_turtle.forward(i * 2)
        spiral_turtle.right(91)

# Execute the drawing
draw_spiral()

# Keep the window open
screen.exitonclick()