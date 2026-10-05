# Curriculum — Python Bytes

This is the **Curriculum** book: the material the coaching team actually teaches in the
course of the club. It is deliberately lean. Advanced, overflow, and historical material
lives in the sibling `Resources/` book, not here.

> Design constraint: **no greedy planning.** The club is an optimization puzzle — keep it
> fun and interesting while keeping it tractable. Resist shoveling advanced material into
> the basic curriculum. When in doubt, it goes to Resources.

## Two tracks

Curriculum has a bicameral structure:

- **`syntax/`** — Python syntax, as a progression from "no knowledge of programming" to
  having the fundamentals at your command. This is where **drill** lives.
- **`projects/`** — Topics where we close the laptop and get out paper and pencil. We think
  and draw around a premise, turn it into a calculation idea, then a concept of code, then a
  program. Python syntax gets integrated as we go. This is where **discovery** and **delight**
  live.

Together, Syntax + Projects are "what we teach."

## The seminal progression

The spine of the Projects track, ordered to avoid magical "type this, it works" leaps:

```
Halfway  →  Fibonacci  →  { Turtle graphics }  →  { Halfway / Fibonacci }  →  Chaos
```

Halfway and Fibonacci teach stateful iterative update (which variable to update first, and
why) with numbers only. Turtle introduces a visual canvas and the idea of using a library.
Then Halfway/Fibonacci return *as geometry* and collapse into the Chaos Game, so the fractal
payoff is earned rather than magic.

## Dependencies

Each project records which syntax modules it needs, as a plain `Needs:` line in its README,
e.g. `Needs: Syntax 1 (variables, average function)`. Projects pull syntax in on demand.

## Conventions

- Prefer `.py` files over notebooks for student-facing material.
- Favor multiple short code examples over one long one.
- Every topic includes a kinesthetic activity (or at minimum a placeholder noting one is needed).
- AI-written code self-identifies: `# AI in use: True`.
- Code is tested in both trinket.io and VS Code; flag results, e.g. `# trinket: OK | vscode: OK`.
