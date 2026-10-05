import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Draw 'Rob' in Block Letters with 3D Effect")

# Create a turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(5)

# Offset for 3D shadow effect
offset = 10

def draw_R(t):
    # Draw main letter R
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    # Diagonal leg
    t.left(135)
    t.forward(70)
    t.left(45)

def draw_O(t):
    # Draw rectangle O
    for _ in range(2):
        t.forward(70)
        t.left(90)
        t.forward(100)
        t.left(90)

def draw_B(t):
    # Draw vertical main stem
    t.left(90)
    t.forward(100)
    
    # Draw upper bowl on right side
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(40)
    
    # Move down to start lower bowl (without drawing)
    t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    
    # Draw lower bowl on right side with reversed turns
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    
    # Return to original orientation
    t.left(180)

def draw_shadow(draw_func, t, x, y):
    # Draw shadow in gray, offset by (offset, -offset)
    t.color("gray")
    move_to(t, x + offset, y - offset)
    draw_func(t)

def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_letter(draw_func, t, x, y):
    # Draw shadow first for 3D effect
    draw_shadow(draw_func, t, x, y)
    # Draw main letter in black
    t.color("black")
    move_to(t, x, y)
    draw_func(t)

# Starting position
start_x = -200
start_y = 0

# Draw letters with 3D effect
draw_letter(draw_R, t, start_x, start_y)
draw_letter(draw_O, t, start_x + 90, start_y)
draw_letter(draw_B, t, start_x + 180, start_y)

t.hideturtle()
turtle.done()
