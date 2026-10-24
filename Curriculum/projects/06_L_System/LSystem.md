# L-System

> For teachers: The payoff is the callback. This draws the *same* Sierpinski
> gasket from the Chaos Game — by a completely different method. Same fractal,
> no randomness at all.

This topic is a two-phase coding challenge that introduces manipulation of strings. It has
the interesting characteristic that phase 1 generates information in a secondhand or incidental
fashion; and then phase 2 interprets that information visually.

We work with a tiny language of four words: `x`, `y`, `+`, `-`. A "sentence" is a
string of them. We start from the simplest sentence, `x`.

## Phase 1 — Rule S (grow the sentence)

Go through the sentence one character at a time and build a new one:

- `x` becomes `y+x+y`
- `y` becomes `x-y-x`
- anything else (`+` or `-`) is copied straight through

Apply it to `x` once, then again:

```
x  →  y+x+y  →  x-y-x+y+x+y+x-y-x
```

In this phase the `x` and `y` do the work; the `+` and `-` just come along for the
ride. Each pass makes the sentence much longer.

## Phase 2 — Rule D (draw the sentence)

Now walk the finished sentence with a turtle. This time the `+` and `-` matter and
the `x` and `y` are ignored:

- `+` turn left 60°, then move forward
- `-` turn right 60°, then move forward
- `x`, `y` do nothing

Run enough passes of Rule S and the turtle traces a familiar shape.

## Punchline

It is the **Sierpinski gasket** — the very fractal we got from the Chaos Game.
There we threw random dots and order emerged. Here there is no randomness at all:
a short rule, applied over and over to a string, produces the same fractal. Two
roads, one destination.

## Variables

- `s` — the current sentence (a string)
- `n` — how many times to apply Rule S
- `bend` — the turn angle (60°)
- `go` — how far the turtle moves per step

## Extensions

- Start from `y` instead of `x`. What changes?
- Change `bend` away from 60°. The shape distorts — try it.
- Invent your own substitution rules. This whole family of string-rewriting
  systems is named for the biologist Lindenmayer — an **L-system** — and the same
  machinery grows plant-like branching figures.
