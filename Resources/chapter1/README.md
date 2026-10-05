# Chapter 1: Pythonic Skills

Boot camp, part 1. Exercise-based muscle building. By the end of this chapter a
student can write a for-loop, define a function, and use a library — all from
memory, without looking anything up.

## Design Philosophy

- Short programs that each do one thing
- Predict before running ("what will this print?")
- Repetition across sessions — these same exercises come back
- No turtle yet (that's Chapter 2). This is text-mode only.

## Skills Covered

1. **Print and strings** — `print()`, string concatenation, `end=""`, `\n`
2. **Variables and types** — int, float, string; `type()`; the bucket metaphor
3. **Input** — `input()` returns a string; `int()` to convert
4. **Arithmetic** — `+`, `-`, `*`, `/`, `//`, `**`, `%` (remainder/modulo)
5. **Logic** — `if` / `elif` / `else`; `==`, `!=`, `<`, `>`, `and`, `or`, `not`
6. **Loops** — `for i in range(n)`, `for item in list`, `while`
7. **Lists** — create, index, append, `len()`, slice
8. **Functions** — `def`, parameters, `return`, calling functions
9. **Libraries** — `import`, `from X import Y`; `random`, `time`, `math`
10. **Putting it together** — small programs that combine 2–3 of the above

## Session Flow (template)

Each session using this chapter material:

1. **Kinesthetic warm-up** (5 min): TBD — see placeholder below
2. **Predict-and-run** (10 min): Show 2–3 short programs, students predict output
3. **Type-along** (15 min): Instructor codes live, students follow
4. **Free practice** (15 min): Exercises from the list below
5. **Show & tell** (5 min): Volunteers show what they got working

## Exercises (progressive difficulty)

### Tier 1: First sessions

```python
# Exercise 1.1: Hello
print("Hello, world!")
name = input("What is your name? ")
print("Nice to meet you, " + name)
```

```python
# Exercise 1.2: Favorite number
s = input("Enter your favorite number: ")
n = int(s)
print(n - 5, "is five less than your favorite number")
```

```python
# Exercise 1.3: Countdown
from time import sleep
for i in range(10, 0, -1):
    print(i)
    sleep(0.5)
print("BLAST OFF!")
```

### Tier 2: Loops and logic

```python
# Exercise 1.4: Is it even?
n = int(input("Give me a number: "))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")
```

```python
# Exercise 1.5: Powers table
for i in range(10):
    print(i, i**2, i**3)
```

```python
# Exercise 1.6: Random choice
from random import choice
animals = ["cat", "dog", "fish", "parrot", "hamster"]
for i in range(5):
    print("You got a", choice(animals))
```

### Tier 3: Functions and libraries

```python
# Exercise 1.7: Define a function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for k in range(20):
    if is_prime(k):
        print(k, "is prime")
```

```python
# Exercise 1.8: Alternating sign
def alternating_sum(n):
    total = 0
    sign = 1
    for i in range(1, n + 1):
        total = total + sign * i
        sign = sign * -1
    return total

print(alternating_sum(10))
print(alternating_sum(100))
```

## Kinesthetic Activity Placeholder

**NEEDED**: A physical activity that reinforces one of the coding concepts above.
Ideas to develop:

- "Human for-loop": Students stand in a line, each one does an action in sequence
- "Variable relay": Pass an object (the "value") between labeled cups ("variables")
- "Modulo clock": Stand in a circle of 6, count off — what's your number mod 6?

## Platform Notes

All exercises above are text-only and should work identically in:
- trinket.io (Python mode)
- VS Code + Python extension
- IDLE

No platform-specific issues expected for this chapter.

## Source Material

Draws from: `Coding1.ipynb` (root), `PBytes_topics_2025_2026.md` (Coding Mechanics
section), `2_Counting/meruprastarah/pascal/README.md` (range/print exercises).
