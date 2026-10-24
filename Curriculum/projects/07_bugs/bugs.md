# Four Bugs

> For teachers: Paper first. Draw the square, step the bugs by hand a few times,
> and let students *see* the inward spiral before any code. The punchline is a
> distance question with a surprising clean answer.

Laptops closed please.

Four bugs sit at the corners of a square table, side *s*. Call them A, B, C, D.
Each bug watches the next one around: A watches B, B watches C, C watches D, D
watches A.

At a signal, every bug takes one tiny step straight toward the bug it is chasing.
Then they all look again — their targets have moved — re-aim, and step again. And
again.

> The bugs are named Alpher, Bethe, Gamow, and Dyson — physicists behind the theory
> of how stars burn. (Yes, bug C is Gamow.)

## What happens

They spiral inward, the square shrinking and twisting, and all four meet at the
center. Pretty, and a little hypnotic.

## The turtle methods

Same three we used in the Chaos Game — pursuit is a perfect fit for them:

- `a.towards(b)` — the angle from bug `a` to bug `b`
- `a.setheading(angle)` — point `a` that way
- `a.distance(b)` — how far apart they are (use it to decide when the chase ends)

The one subtlety: each tick, **re-aim every bug first, then move them all one
step**. They march in lockstep. If one bug moves before the others re-aim, the
chase goes crooked.

## Punchline

How far does each bug walk before they meet? Students will expect something messy
with a spiral. Measure it in the code. The answer is exactly **one side of the
square** — distance `s`, clean and surprising. Worth stopping on and arguing about
why.

## Extensions

- **Any regular n-gon:** put the bugs on the corners of a triangle (3), a pentagon
  (5), a hexagon (6) — any regular *n*-gon of side *s*, each bug chasing the next.
  What is the walk distance now? What about the extreme cases: *n* very large (the
  table becomes a circle), or *n* = 2 (two bugs on a wire / tightrope, facing each
  other)? A good open-ended coding project — work out the corner positions yourself.
- **Diagonals:** draw the square's two diagonals. How many does a bug cross on its
  way in? (A thinking problem, not a coding one.)
- **Step size:** make the step bigger or smaller. Does the meeting point move?

## Kinesthetic activity

> Placeholder — needs development. Sketch: four students stand at the corners of a
> taped square on the floor. On "go," each takes one small step toward the student
> they are chasing, then everyone re-aims and steps again, in rounds called by the
> coach. The class watches the square shrink and rotate into the center — the
> pursuit spiral, performed.
