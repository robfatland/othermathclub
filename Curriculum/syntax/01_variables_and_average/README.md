# Syntax 1 — Variables and the Average Function

The very first syntax module. Two related parts.

## Part A — Mental Memory Model (MMM): writable boxes

A variable is a **labelled box you can write into**. The label is the name; the value is
what's inside right now. The two moves that matter:

- **Write / overwrite:** `score = 10`, then later `score = 25` — same box, new contents, old
  value gone.
- **Read:** using the name reads whatever is currently in the box.

Keep it concrete. Draw the boxes. Students should be able to say out loud "the box labelled
`a` holds 4" before any code runs.

## Part B — A function that returns an average

A function is a **named recipe**: hand it values, it hands one back via `return`.

```python
def average(first, second):
    return (first + second) / 2
```

The key idea to plant: the returned value is itself a value — it can go straight into a box
(`midpoint = average(0, 1)`). This is the hook Project 1 (Ms. Halfway) depends on.

## Why these two together

Project 1 needs exactly this and nothing more: boxes to hold *where she is / wants to go /
pauses*, and a function to compute the halfway point. The module is sized to the project, not
to "everything about variables."

## Kinesthetic activity

**Placeholder — needs development.** Sketch idea: students *are* the boxes. Each student holds
a card (the label) and a number they can erase and rewrite. "Box `a`, show 4. Box `b`, show
10. Box `total`, you are `a + b` — go read them and write your number." Overwriting a box =
erasing and rewriting the card. The `average` recipe is a student who walks to `a` and `b`,
adds, divides by two, and announces the result.

## Platform testing

`# trinket: OK | vscode: OK` — plain variables, arithmetic, one function. No library imports.
