# Python Syntax Skills — the "Automatic by February" list

`Syntax/` covers the basics; plus you will benefit from learning some library commands. This document covers what you should know from memory: Then you can say you "speak Python". By *February* is a good goal to have this down. The material is presented in a logical order (we hope!). When you get this down: Python coding will not be a "look it up" process for you; but this means you will need to practice. When you can write a working for-loop on a blank piece of paper you will know you are getting somewhere!  


The projects (see `projects/`) refer to the learn-by-memory table below. We also have **beyond the automatic stuff** at the bottom of this document; plus more good stuff in **Resources**.



## Coding Concepts and Rules Of Thumb


- The computer has a **mind space** where we can set up little worlds...
    - ...and start them into action
- These are called **programs** (like stories)... 
    - ...and they are made of **code** (like sentences)
- Code **executes** as a sequence of actions inside the computer
    - ...so our goal is to convert our ideas to working code
- Code must follow proper format: **syntax**
- Code must also follow rules of logic
- If we make mistakes (**bugs**): We stop everything to fix them...
    - ...and this is called debugging
- If our program does what we intend: We celebrate (shout, dance for joy)
    - ...and then we often think of something else to add or change
    - ...this is called *being a software developer*
- We tend to succeed faster if we use paper and pencil first


## The list of things to know: Mostly syntax, plus some library stuff


| # | Skill | Automatic means you can, from memory... |
|---|-------|------------------------------------------|
| 1 | **Variables** | make a box, read it, overwrite it (`x = 0`, then `x = 25`) |
| 2 | **`print()`** | text, values, multiple values; `end=""` to stay on one line |
| 3 | **Arithmetic** | `+ - * /`; `/` gives a float |
| 4 | **Functions** | `def name(args):` and `return` a value you can use directly |
| 5 | **Turtle graphics** | `Turtle()`, `forward`, `left` etc: A drawing vocabulary to learn |
| 6 | **`input()` returns a string** | `input()`, then `int()` it to do math |
| 7 | **`for` / `while` loops** | `for i in range(10):` and `while condition:` |
| 8 | **`if` / `elif` / `else`** | branch on a condition |
| 9 | **`range()` variants** | `range(n)`, `range(a, b)`, `range(a, b, step)`, `range(a, b, -1)` |
| 10 | **`for`-loop over a list** | `for item in things:` |
| 11 | **Nested loops** | a loop inside a loop; inner depends on outer (`for j in range(i)`) |
| 12 | **Type conversion** | `int()`, `str()`, `float()` |
| 13 | **Reassignment / update order** | `x = p` as a *reset*; order matters |
| 14 | **Lists: make / index / append / len** | `[]`, `a[0]`, `a[-1]`, `.append()`, `len()` |
| 15 | **Strings as lists of characters** | `s[0]`, `len(s)`, `for c in s`, join with `+`; a string is like a list of letters |
| 16 | **Copying a list** | `new = old[:]` — a copy, not a reference |
| 17 | **Comparison + boolean operators** | `== != < >`, `and`, `or`, `not` |
| 18 | **Modulo `%`** | remainder; even test (`n % 2 == 0`), divisibility |
| 19 | **`import` / `from` import** | `import turtle`, `from random import choice` |
| 20 | **`random`** | `randint`, `choice` |
| 21 | **`time`, `math`** | `sleep` (time); `sqrt`, `pi`, trig (math) |

## How the seminal progression draws on the list

```
Halfway    → 1, 2, 3, 4, 13          (boxes, print, arithmetic, average function, reset/update order)
Fibonacci  → 1, 2, 3, 13             (three-variable update order; the reset lesson, harder)
Turtle     → 5, 7, 19                (turtle is the new idea; a loop drives the drawing)
Chaos      → 5, 10, 14, 20           (fixed points, random.choice, jump halfway, draw a dot)
```

Halfway and Fibonacci are about the **reset** — repeating a block of code some number of times,
not loops as a skill. (We just repeat the block ten times; a student can meet them before loops
are automatic.) Turtle introduces one new thing: the drawing canvas. Chaos adds lists +
randomness. That is the anti-greedy pacing.

## Beyond the automatic stuff

This is good to recognize even if you do not memorize it. 


- f-strings / `%` formatting (we use `%` formatting in Meru Prastarah, but as a recipe, not a
  memorized skill)
- `.towards()`, `.setheading()`, `.distance()` and other turtle *methods* (project-specific)
- dictionaries, tuples, comprehensions, slicing beyond `[:]`
- classes / objects, file I/O, exceptions, `requests` (all → later or Resources)
