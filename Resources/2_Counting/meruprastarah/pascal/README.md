# Python Pascal Triangle (Meru Prastarah)

Consolidated project write-up. This was previously three separate files (`README.md`,
`README1.md`, `README2.md`) that were actually the notes from three successive sessions, not
alternatives. They are merged here in order. Instructor scratch code lives in `rob_notes.py`.

> `rob_notes.py` is working scratch, not a clean solution — it has an early `sys.exit(0)` and
> two buried triangle implementations. Keep for reference; do not hand to students as-is.

---

## Session 1 — The four pieces, and getting started

### Overview

We want our program to print the Pascal triangle like this:

```
                 1
             1       1
         1       2       1
     1      3        3       1
 1       4       6       4       1
```

To finish the project we need four things:

- A way to `print()` without a built-in line feed, so we can glue a row together from pieces:

```
 1       4       6       4       1
```

  instead of:

```
 1
         4
                 6
                         4
                                 1
```

- A way to `print()` bigger numbers the same width as small numbers, so `462` (three wide) and
  `5` (one wide) line up:

```
     462
       5
```

- A way to count automatically: the `range()` function.
- A way to build the *next* row of the triangle from the current row (held as a list).

Remember to use IDLE!

### Part 1: Printing without a line feed

```
print("fred")
print("flintstone")
print("was here")
```

Now change the print so `flintstone` follows `fred` directly:

```
print("fred", end="")
print("flintstone")
print("...was here")
```

Almost perfect — there is still one small problem. See if you can fix it.

### Part 2: Printing numbers the same width

Copy and run this. It uses four variables — bonus: what is their **type**?

```
a1 = 5385
a2 = 3
a3 = 12
a4 = 946728348

print('\nmessy version:\n')

print(a1, a1)
print(a2, a1)
print(a3, a1)
print(a4, a1)
```

The numbers jam together. Add these lines to line them up with a fixed 9-character width:

```
print('\npretty version:\n')

print('%9d' % a1, '%9d' % a1)
print('%9d' % a2, '%9d' % a1)
print('%9d' % a3, '%9d' % a1)
print('%9d' % a4, '%9d' % a1)

print('\n')
```

### Part 3: Counting using `range()`

`range(5)` counts `0, 1, 2, 3, 4` — starts at zero, stops just below the number you give.

```
my_counter = list(range(7))
print(my_counter)
```

Experiment with `range(2, 9)`, `range(4, 21, 3)`, and `range(19, -6, -2)`. What do they do?
And what does this do?

```
q = 10
a = list(range(q))
for b in a:
    print(' ' * (30 - 2*b), 'cow')
```

### Part 4: Creating the next row from the current row

Suppose row 3 is in a list called `row`:

```
print(row)
[1, 2, 1]
```

The next row has four elements. Make a new row of all `1`s:

```
new_length = 4
new_row = [1]*new_length
print(new_row)
```

Then print each element:

```
print(new_row[0])
print(new_row[1])
print(new_row[2])
print(new_row[3])
print(new_row[4])
```

This has a bug (an index error) you will need to fix. Finally, note the key move:

```
new_row[1] = row[0] + row[1]
print(new_row[1])
```

### What we began with (first-meeting recap)

- Rob's first rule: put your computer away (get out a piece of paper).
- Rob's second rule: don't do what you're trying to do; do something easier.

Variables are little buckets with a label, contents, and a `type` (integer, string). Programs
run top-down (loops jump around). The triangle starts with a `1` at the top, with invisible
zeros on either side, so each number is the sum of the two above it. We warmed up with:

```
for i in ['pig', 'dog']:
    print(i)
```

then numbers in place of strings:

```
for i in [0, 5, 10, 15, 20, 25]:
    print('m'*i, 'horse')
```

then reversed, for the **Aha!** that the indent shrinks just like the triangle needs:

```
for i in [25, 20, 15, 10, 5, 0]:
    print('m'*i, 'horse')
```

---

## Session 2 — A stepping-stone, then a working triangle

The Pascal project combines Python lists with two `for`-loops: an outer loop over rows, and an
inner loop across each row that must grow each time. A lot to figure out — so first a simpler
program that prints the squares of a chess board (rows numbered, columns lettered):

```
letters = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

print("\nchess board\n")

for i in range(1,9):
    print(' '*12, end = '')
    for j in range(8):
        square_label = letters[j] + str(i)
        print("%5s" % square_label, end = '')
    print("")
```

Now change one line to make it resemble Pascal — predict what happens:

```
    for j in range(i):
```

Note we used a list for the letters but the counting variable `i` for the row numbers, and
`str(i)` to change the integer `i` into a string so it could join `square_label`.

Here is the Pascal triangle version (left-justified):

```
# This uses a simple print() so the triangle is left-justified

for r in range(1,11):               # r will be 1, 2, 3, ..., 10
    row = []                        # row[] is an empty list
    for c in range(1, r + 1):       # c will be 1, 2, ..., r
        if c == 1:
            row.append(1)           # left side of the triangle is 1
        elif c < r:
            row.append(row_above[c-2] + row_above[c-1])
                                    # middle of the triangle: add 2 numbers
        else:
            row.append(1)           # right side of the triangle is 1
        print("%4d" % row[-1], "  ", end = "")
    print("")

    # now the row[] list contains all the numbers in this row
    row_above = row[:]              # this makes row_above[] a copy of row[]
```

Helpful to know:

- Everything from `#` onward is a comment.
- `row[-1]` means "the last element of `row[]`." If `row = [0, 3, 7, 12]` then `row[-1]` is `12`.
- Copy a list with `new_list = old_list[:]`.
- Lists index from `0`, which gets confusing when rows start at 1 — write it out by hand:
  - If `r = 7` and `c = 4`, we are at the 4th number of row 7.
  - Its value is the sum of the 3rd and 4th numbers of row 6, held in `row_above[]`.
  - `row_above[] = [1, 5, 10, 10, 5, 1]`, so the 3rd and 4th are `row_above[2]` and `row_above[3]`.
  - Hence `row_above[c-2] + row_above[c-1]` → `10 + 10 = 20`.
  - Row 7 is `1  6  15  20  15  6  1` — the 4th number is indeed `20`.

---

## Session 3 — Finishing, row sums, and the next problem

### Finishing the program (centered print)

Suppose rows 1–4 are printed and you are on row 5, having printed `1  4  6` so far. The next
number is `4`, which is `new_row[3]` if the full row `[1, 4, 6, 4, 1]` is in `new_row`. But we
can't hard-code `new_row[3]` — we use a loop variable. With an outer `i` loop over rows:

```
for i in range(1, 11):
```

and an inner `j` loop across the row:

```
    for j in range(i):
```

when `i` is `5`, `j` runs `0, 1, 2, 3, 4`. To print `new_row[3]` we print `new_row[j]`:

```
        print("%3d" % new_row[j], "   ", end="")
```

and after the row, a line feed:

```
    print("")
```

### Building `new_row[]` from `row[]`

Start with an empty `row` outside the loops, loop `i` from 1 to 10, and build a fresh all-ones
`new_row` of length `i` each time:

```
row = []
for i in range(1, 11):
    new_row = [1] * i
```

Fix the middle elements before printing:

```
    for j in range(1, i - 1):
        new_row[j] = row[j - 1] + row[j]
```

When `i` is `5`, `j` is `1, 2, 3`. For `j = 1`, `new_row[1] = row[0] + row[1] = 1 + 3 = 4`
(since `row` is `[1, 3, 3, 1]`). Then copy forward for the next row:

```
    row = new_row[:]
```

The `[:]` makes a full copy. (Think of building a volcano — the next layer of lava sits on all
the previous layers.)

### Extra challenge: row sums

At the far left of each row, print the sum of that row. Row `[1]` → `1`; row `[1, 1]` → `2`.
Look for the pattern (powers of two). Useful:

```
a = [4, 5, 10]
my_sum = sum(a)
print(my_sum)
```

Does `print(sum(a))` also work? What about `sum([4, 5, 'pig'])`?

### Bonus: counting spiral

Count from 1 to 36 placing numbers in a square spiral — as a program that figures it out, not
36 print statements:

```
  21   22    23    24    25    26
  20    7     8     9    10    27
  19    6     1     2    11    28
  18    5     4     3    12    29
  17   16    15    14    13    30
  36   35    34    33    32    31
```

### Next problem

(Open — this was the end of the original notes.)

---

## Connections to flag

- **Row sums are powers of two** — a clean numeric Aha that returns in the binary / cellular
  automata material.
- **Meru Prastarah → Fibonacci → Sierpinski**: summing shallow diagonals gives Fibonacci; the
  mod-2 (even/odd) mask of MP is the Sierpinski gasket, which also matches the XOR universe.
  These are the payoffs that make MP a strong future **Curriculum** candidate (Chapter 4 in the
  old plan).
