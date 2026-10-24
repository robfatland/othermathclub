# Turtle

> For teachers: Low-key on purpose. Turtle is where students meet a *library*
> and a drawing canvas. The real payoff for the canvas comes later, at Chaos.

Laptops open this time.

So far we have worked with numbers. Now we draw.

`turtle` is a library built into Python — nothing to install. It is friendly and
easy to picture: a turtle holds a pen and crawls around the screen leaving a line.
You tell it to go forward, turn, lift the pen, change color.

It is also slow, and not built for games. When we want real games later we reach
for a different library (pygame). For now, friendly beats fast.

## Driving the turtle

A handful of commands do most of the work:

- `t.forward(100)` — crawl forward 100 steps, drawing
- `t.left(90)` / `t.right(90)` — turn in place
- `t.penup()` / `t.pendown()` — stop and start drawing
- `t.goto(x, y)` — jump to a spot
- `t.color("blue")` — change pen color

A square is four `forward`s and four `left(90)`s. Students see the pattern and
reach for repetition — which is the door to the loop at the end.

## Build it in stages

The worksheet (`Curriculum/ALO_Handouts/Handout2_2026.md`) walks students through
building the program a piece at a time: square, then circle, then dot, then the
spiral. Build one piece, run it, watch it draw, add the next.

## Punchline

The program ends with a loop:

```
for step in range(60):
    t.forward(step * 4)
    t.right(91)
```

Each line is a little longer and the turn is 91 degrees, not 90. That one extra
degree is what makes it spiral instead of closing into a square. Small change,
surprising picture — worth stopping on.
