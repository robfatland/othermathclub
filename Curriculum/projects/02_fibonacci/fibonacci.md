# Fibonacci

> For teachers: This is the low-drama sequel to Ms. Halfway. Same shape, fewer
> moving parts. A student who caught on last time should get most of the way on
> their own.

Needs: Ms. Halfway (the `average` function, variable update, the reset idea).

Laptops closed please.

We build a sequence of numbers. Start with two: `1` and `1`. Each new number is
the sum of the previous two.

```
1  1  2  3  5  8  13  21  34  ...
```

Do a few on paper. Students see the rule fast: add the last two to get the next.

## The function

Ms. Halfway gave us `average(a, b)`. Here we want a function that adds two numbers.
We call it `addemup` — not `sum`, because `sum` is already a Python word and we
don't want to clobber it.

```
def addemup(a, b):
    return a + b
```

## Three variables

Ms. Halfway used two numbers and updated them in the right order. Fibonacci uses
three. Call them `a`, `b`, `c`.

- `c` is the new number: `c = addemup(a, b)`
- Then everyone shifts down: `a` becomes `b`, `b` becomes `c`.

Order matters, same as before. Shift `a` first, then `b`:

```
a = b
b = c
c = addemup(a, b)
print(a, b, c)
```

As with Ms. Halfway, students can copy-paste that block and watch the numbers
climb. This time we *do* reach for a loop — the copy-paste pain from last project
is the motivation.

## Variables

- `a` — the older of the two previous numbers
- `b` — the newer of the two previous numbers
- `c` — the next number (their sum)

## Stretch goal: the asymptote

Ms. Halfway settled at 1/3. Fibonacci never settles — the numbers grow forever.
But the *ratio* of each number to the one before it does settle. Have students
print `b / a` each time through the loop and watch it home in:

```
... 1.618 ... 1.618 ... 1.618 ...
```

That number is the golden ratio. It is a good bonus for a student who wants more.
