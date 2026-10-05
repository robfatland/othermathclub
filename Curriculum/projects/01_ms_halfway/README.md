# Project 1 — Ms. Halfway

**Needs: Syntax 1 (variables, average function)**

First project in the seminal progression:

```
Halfway  →  Fibonacci  →  { Turtle }  →  { Halfway / Fibonacci }  →  Chaos
```

## The premise (paper and pencil first)

Ms. Halfway stands at a spot `x`. She wants to reach a destination `d`. But she only ever
walks to the point **halfway** between where she is and where she wants to go. Then she
treats *that* spot as her new standing point and does it again.

Rob's first rule applies: put the computer away, draw the number line, and step it by hand a
few times before any code.

## Variables

- `x` — where she is
- `d` — where she wants to go
- `p` — where she pauses (the halfway point)

## The build

1. Start: `x = 0`, `d = 1`, `p = average(x, d)` → `p` is `0.5`.
2. **The reset.** This is the lesson. After computing the pause point, she *becomes* someone
   standing at that point: `x = p`. Spend time here — "which box changes, and when?" is the
   same update-ordering thinking that returns in Fibonacci and the Chaos Game.
3. Repeat the step **ten times** with a loop, then `print(x)`.

`average` is defined **inline** so the project runs on its own, but it is the same recipe
from Syntax 1 — point that out.

## The punchline / line of inquiry

Running the code is the *beginning*, not the end:

- After ten halvings, how close to `d = 1` is she? Does she ever exactly arrive?
- Change `d` (7, 100) and the start `x`. What stays true?
- Foreshadow: if `d` were chosen at random each step from a few fixed targets, the trail of
  pause points draws something unexpected. That is the Chaos Game — but not yet. No greedy
  planning.

## Connection to flag

The reset (`x = p`) rehearses the exact "update the right variable in the right order"
discipline that Fibonacci needs with three variables and that the Chaos Game needs to iterate
a moving point. Same muscle, three times, each with a bigger payoff.

## Kinesthetic activity

**Placeholder — needs development.** Sketch idea: tape a number line on the floor, `0` at one
end, `1` (the destination `d`) at the other. A student stands at `x`. Each round, a second
student stands at the halfway point `p` (literally pacing out the midpoint). Then the first
student walks to join them — that walk *is* the reset `x = p`. The class watches her approach
but never quite reach `d`.
