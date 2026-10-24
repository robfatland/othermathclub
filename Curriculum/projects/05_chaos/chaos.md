# The Chaos Game

> For teachers: This is the payoff of the whole first arc. Make the students
> *predict* the outcome before running. The surprise only lands if they commit
> to a guess first.

Laptops closed please. Paper and pencil.

A painter named Egon wants to make a dot painting on the town square. He sets
three paint cans on the ground as the corners of a big triangle. He stands
somewhere, picks a corner at random, walks **halfway** to it, and dabs a dot.
Then he picks another corner at random and does it again. And again. Thousands
of times.

This is Ms. Halfway again — go halfway toward a destination — except the
destination is a *random corner* each step.

## The procedure

One step is:

1. Pick a corner at random.
2. Walk halfway from where you stand to that corner.
3. Dab a dot.

Then repeat from your new spot.

## Driving the turtle

We let the turtle do the aiming instead of computing the midpoint by hand. Three
turtle commands carry the project:

- `t.towards(target)` — the direction from the turtle to the target
- `t.setheading(angle)` — point the turtle that way
- `t.distance(target)` — how far to the target (halve it to go halfway)

So "walk halfway to the corner" becomes: aim at it, measure the distance, go
half.

## Predict first

Before running, ask: **what will the picture look like?** A random process —
surely a shapeless cloud? Make everyone commit to a guess.

Then run it. The dots do *not* fill the triangle. A pattern of ever-smaller
triangles appears, holes inside holes. That is the punchline: order out of pure
randomness.

We start Egon *outside* the triangle on purpose. His first few dots fall as
strays between the start and the pattern, then he snaps onto the gasket and stays
there. Those stray dots are the clue: every "halfway" jump pulls him in toward the
triangle, so wherever he began, the pattern wins.

## Fractal

The shape has a name and a property. It is the **Sierpinski gasket**, and it is a
**fractal** — zoom in on any part and you find a smaller copy of the whole thing.
The same triangle-in-triangle structure repeats at every scale.

## Dot size matters

The dot size makes or breaks the picture. Too big and the dots merge into a solid
black triangle — the structure drowns. Too small and it reads as dust. Have
students try `DOT_SIZE` of 6, then 1, then settle around 2.

## Extensions

- **Four corners** instead of three (a square). Does a fractal appear? Try it.
- **A different fraction** than halfway. Try 1/3, try 2/3. What about a jump
  bigger than 1? A negative jump? Explore the fraction on `[0, 1]`, then past
  the ends.
