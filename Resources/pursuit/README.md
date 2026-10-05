# Pursuit

Canonical home for the **pursuit** family of problems: one thing chasing another, where the
paths traced out ("pursuit curves") are often surprising and pretty. Consolidated here from
material that was previously scattered across `4_Models/pursuit/`, `PythonBytes/`, and inside
`Coding2.ipynb`.

Three flavors live here, from simplest to richest:

| File | What it is |
|------|------------|
| `simple_pursuit_two_turtles.py` | **Simple pursuit game** — two turtles. A wandering target, one pursuer that steers toward it with distance-dependent speed. The gentlest entry point. |
| `four_bugs.py` | **Four Bugs** — the classic. Four bugs at the corners of a square, each walking toward the next. Fully commented teaching version. |
| `four_bugs_compact.py` | The same Four Bugs problem written compactly with a list of turtles. The "after they get it, show them the tidy version" companion. |
| `random_bugs.py` | **Random bugs** extension — N turtles wander, then all turn toward a common point. |
| `wolf_and_duck.py` | **Wolf and Duck** — a duck in a round pond, a wolf on the shore running toward the duck's shadow. Extracted from `Coding2.ipynb`. Uses a reward function + gradient ascent. The advanced member of the family. |

## The problem (Four Bugs)

Four bugs — A, B, C, D — sit at the corners of a square table of side *s*. Each faces the next
bug counterclockwise (A→B, B→C, C→D, D→A). At a signal all walk at the same tiny step size,
each always heading straight at the bug it chases. They constantly re-aim because their targets
are also moving. They spiral inward and meet at the center. How far has each walked?

> The bugs are named Alpher, Bethe, Gamow, and Dyson (yes, bug C is Gamow, not "Camow") — the
> physicists behind the theory of how stars burn.

Rob's first rule applies: paper first. Draw the square, step it by hand a few times, and *see*
the inward spiral before writing code.

## The turtle methods that make it work

Pursuit is a natural fit for turtle graphics because the library hands you exactly the three
methods you need:

- `a.towards(b)` — the angle from turtle `a` to turtle `b` (in degrees).
- `a.setheading(angle)` — point `a` in that direction.
- `a.distance(b)` — how far apart they are (use it to decide when the chase is over).

The one subtlety: on each step, **re-aim every bug first, then move them all one step**. Don't
let one bug take extra steps — they march in lockstep.

## Wolf and Duck (the advanced member)

A duck swims in a circular pond of radius *R* at speed *vd*. A wolf runs around the shore at
speed *vw* (faster: `vw = 4*vd` in the code), always toward the duck's *shadow* — the point on
the shore at the duck's current angle. The duck wants to reach shore at a point far enough
ahead of the wolf to escape and fly away.

The classic insight: the duck should first spiral out to a radius of about **R/4** (precisely
`R*vd/vw`), where it can out-maneuver the wolf's angular speed, then break for the nearest
shore. `wolf_and_duck.py` finds the escape path by **gradient ascent** on a reward function
with a plateau between an inner radius (~0.22 R) and the outer R/4 ring — connecting the
pursuit problem to optimization. See the `DuckCanFlyAway()` test for the escape condition.

## Extensions (from the original write-up)

- **Diagonal crossings:** draw the two diagonals of the square. How many does a bug cross on
  its way to the center? (A thinking problem, not a coding one.)
- **Other shapes:** triangle (3 bugs), hexagon (6), tightrope (2 bugs facing each other). What
  is the walk distance for a regular *n*-gon of side *s*?
- **Random bugs:** place N bugs at random, each chasing the next. Version 1, all same speed.
  Version 2, speed proportional to distance to the chased bug. What changes? (`random_bugs.py`)

## Kinesthetic activity

**Placeholder — needs development.** Sketch idea: four students stand at the corners of a taped
square on the floor. On "go," each takes one small step straight toward the student they're
chasing, then everyone re-aims and steps again, in rounds called by the coach. The class
watches the square shrink and rotate into the center — the pursuit spiral, performed.

## Related assets

Images for this topic: `Resources/A3_Images/Mathematics/Pursuit/`.
