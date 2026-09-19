import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1200, 800)

t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.pensize(2)

def draw_3d_text(text, start_x, start_y):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    
    # Main text
    t.color("cyan")
    t.write(text, font=("Arial", 48, "bold"))
    
    # 3D shadow effect
    t.penup()
    t.goto(start_x + 3, start_y - 3)
    t.pendown()
    t.color("white")
    t.write(text, font=("Arial", 48, "bold"))
    
    # Another shadow layer
    t.penup()
    t.goto(start_x + 6, start_y - 6)
    t.pendown()
    t.color("gray")
    t.write(text, font=("Arial", 48, "bold"))

# Draw "audacious text"
draw_3d_text("AUDACIOUS", -300, 50)
draw_3d_text("TEXT", -150, -50)

screen.exitonclick()