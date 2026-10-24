# XOR Universe

This topic builds a one-dimensional universe inside our Python program and lets it
evolve under a logical rule. We work up to it through three rules — AND, OR, and
finally XOR — because the first two are boring and that is the point.

- We have a line of cells in one dimension, initially empty _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
- Maybe this continues in both directions for a very long way
- We will call this the Empty Universe.
- Each cell is either empty or contains a dot...
    - ...but when the Universe begins there are no dots; just empty cells
- Some time passes... but nothing changes: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
- Some more time passes... and a miracle occurs!
    - The miracle is that one of the cells has a dot
    - This is going to be "the big bang"
    - This time around the Universe gets only one such miracle
    - Here is the new Universe: _ _ _ _ _ _ _ . _ _ _ _ _ _ _
- Some more time passes and the Universe begins to evolve...
    - It evolves following a Law of Nature
    - The law looks at each cell's two neighbors: the one to the **left** and the
      one to the **right**

## Two parents, then three

> For teachers: An earlier version offset each row by half a cell, so a new cell
> had just **two** parents sitting above-left and above-right. We are not doing
> that this time. We keep the rows aligned and let a cell look at its two *outer*
> neighbors — the generalization from 2 parents to 3 (left, center, right, with
> center along for the ride). Same spirit, cleaner to reason about.

## Three laws

Each law decides whether a cell is filled next tick, from its left and right
neighbor.

**AND** — filled only if *both* neighbors are filled.

Start from one dot. The dot has no place where both neighbors are filled, so the
whole universe goes empty on the very next tick. Over in one step. Boring.

**OR** — filled if *either* neighbor is filled.

Now the dot spreads both directions every tick and nothing ever turns off. The
universe fills into a solid triangle. Boring the other way — too dense.

**XOR** — filled if *exactly one* neighbor is filled, but **not both**.

This is the interesting one. "Exclusive or": left or right, but not the pair.

| left | right | next |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Time runs down the page

We print the universe one row at a time. A filled cell is `o`, an empty cell is a
space. Each new row sits below the last, so time marches down the screen.

## The edges

The universe is a ring — the far-left cell's left neighbor is the far-right cell.
Python gives us this almost for free:

- `row[i - 1]` — index `-1` already means "the last cell", so the left edge wraps.
- `row[(i + 1) % WIDTH]` — the modulo `%` sends the right edge back to `0`.

## Predict first, then run

Start from one dot (the Big Bang) and run XOR. **What shape appears?** Make a guess
before running.

## Punchline

It is the **Sierpinski gasket** — the same fractal as the Chaos Game and the
L-System. Random dots gave it to us; string rewriting gave it to us; now a single
logic gate gives it to us. Three completely different roads, one fractal.

## Extensions

- Start from random cells instead of a single dot.
- Grow `WIDTH` and `TICKS` (keep `WIDTH` odd so there is a true middle).
- Invent your own rule from the two neighbors. Which ones are boring? Which spark?
