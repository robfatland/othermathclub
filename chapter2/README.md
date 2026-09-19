# Chapter 2: Drawing with Python

Boot camp, part 2. We drop the other shoe: Here are the methods of turtle graphics,
and here is a list of things for you to draw — up to and including multiple turtles
interacting on the canvas.

## Design Philosophy

- Chapter 1 gave you the logic; Chapter 2 gives you the payoff
- Every exercise produces something visual — immediate gratification
- Build from simple (one turtle, straight lines) to complex (multiple turtles, color, interaction)
- The turtle library teaches OOP concepts implicitly (objects, methods, state)

## Prerequisites (from Chapter 1)

- `for` loops with `range()`
- Variables (especially changing them inside loops)
- Functions (`def`)
- `import` / `from X import Y`
- `random` library basics

## Skills Covered

1. **Turtle basics** — `Turtle()`, `forward()`, `left()`, `right()`, `goto()`
2. **Pen control** — `penup()`, `pendown()`, `pencolor()`, `width()`
3. **Drawing with loops** — polygons, stars, spirals
4. **Color** — RGB tuples, changing color inside loops
5. **Speed and rendering** — `tracer(0, 0)`, `update()`, `speed()`
6. **Multiple turtles** — create a list of turtles, each with its own behavior
7. **Randomness in drawing** — `randint()` for position, color, angle
8. **Composition** — combining loops, functions, and turtles into a scene

## Session Flow (template)

1. **Kinesthetic warm-up** (5 min): See placeholder below
2. **Demo & predict** (10 min): Show a short turtle program, students predict the drawing
3. **Type-along** (15 min): Build up a drawing step by step
4. **Challenge list** (20 min): Students pick from the menu below
5. **Gallery walk** (5 min): Students show their screens, others walk around

## Turtle Method Reference

```python
from turtle import Turtle, Screen

screen = Screen()
t = Turtle()

# Movement
t.forward(100)       # move forward 100 pixels
t.backward(50)       # move backward 50 pixels
t.left(90)           # turn left 90 degrees
t.right(45)          # turn right 45 degrees
t.goto(x, y)        # go to coordinates (x, y)
t.setheading(angle)  # point in direction (0=east, 90=north)

# Pen
t.penup()            # lift pen (move without drawing)
t.pendown()          # lower pen (draw when moving)
t.pencolor("red")    # set pen color by name
t.pencolor(0.5, 0, 1)  # set pen color by RGB (0-1 scale)
t.width(3)           # set line thickness

# Stamps and dots
t.dot(20)            # draw a filled circle, diameter 20
t.stamp()            # stamp turtle shape at current position

# Speed / rendering
t.speed(0)           # fastest animation
screen.tracer(0, 0)  # turn off animation (draw all at once)
screen.update()      # show the result after tracer(0,0)

# Interaction (advanced)
t.towards(x, y)      # angle toward a point
t.distance(x, y)     # distance to a point
```

## Drawing Challenges (progressive)

### Tier 1: One turtle, basic shapes

1. **Square** — `forward(100)` + `left(90)`, four times
2. **Triangle** — equilateral, any size
3. **Polygon** — write a function `polygon(sides, size)` that draws any regular polygon
4. **Staircase** — alternating forward and left/right to make steps
5. **Spiral** — forward distance grows each step

### Tier 2: Color and loops

6. **Rainbow spiral** — change `pencolor()` each iteration using a color list
7. **Concentric squares** — nested squares with different colors
8. **Star** — 5-pointed star (hint: `left(144)`)
9. **Grid of dots** — nested loops, `penup/pendown`, `dot()`
10. **Random walk** — random angle + fixed step, 200 iterations

### Tier 3: Multiple turtles and interaction

11. **Two turtles race** — both go forward random amounts each tick
12. **Chase** — turtle A moves toward turtle B using `towards()`
13. **Falling from the sky** — one turtle descends, drifting with `randint()`
14. **Flock** — 5+ turtles each doing their own random walk
15. **Chaos Game preview** — (bridge to Chapter 3) three fixed points, one turtle jumps halfway to a random choice each step

## Kinesthetic Activity Placeholder

**NEEDED**: Physical activity reinforcing turtle/drawing concepts. Ideas:

- "Be the turtle": One student gives L/R/Forward commands, another walks them
- "Human polygon": N students form a regular polygon by each turning the same angle
- "Guess the drawing": Instructor reads turtle commands aloud, students sketch on paper what they think it draws

## Platform Notes

- **trinket.io**: Turtle works natively. Use `from turtle import *` style for simplicity.
  Note: `tracer(0,0)` / `update()` may behave slightly differently. Test.
- **VS Code**: Requires a display. Works on localhost. Turtle window opens separately.
- **IDLE**: Full turtle support, this is its natural habitat.

Flag: `# trinket: [status] | vscode: [status]` — to be filled per exercise after testing.

## Source Material

Draws from: `Coding1.ipynb` (turtle section), `Coding2.ipynb` ("Falling From The Sky"),
`PBytes_topics_2025_2026.md` (turtle library methods section).
