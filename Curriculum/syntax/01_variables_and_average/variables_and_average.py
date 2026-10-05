# AI in use: True
# trinket: OK | vscode: OK
#
# Syntax Module 1 — Variables (writable boxes) and the average function
# Python Bytes / Curriculum
#
# Two related ideas:
#   Part A. A variable is a labelled box you can write into (and overwrite).
#   Part B. A function takes numbers in and hands a number back: average(a, b).

# ----------------------------------------------------------------------
# Part A — The Mental Memory Model (MMM): writable boxes with labels
# ----------------------------------------------------------------------
# Picture a box. Write a label on the outside. Put a value inside.
# The label is the variable name. The value is what's in the box right now.

score = 10          # make a box labelled "score", put 10 in it
print(score)        # look inside the box: 10

# You can OVERWRITE a box. The old value is gone; the new value is in.
score = 25          # same box, new contents
print(score)        # 25

# You can make as many boxes as you like, each with its own label.
a = 4
b = 10
print(a)            # 4
print(b)            # 10

# A box can be filled using OTHER boxes.
total = a + b       # read box a, read box b, add, write the result into total
print(total)        # 14


# ----------------------------------------------------------------------
# Part B — A function that returns the average of two numbers
# ----------------------------------------------------------------------
# A function is a named recipe. You hand it values; it hands one back.
# "return" is how the recipe hands its answer back to you.

def average(first, second):
    return (first + second) / 2

# Use it. The returned value can go straight into a box.
midpoint = average(0, 1)
print(midpoint)             # 0.5

print(average(4, 10))       # 7.0
print(average(10, 10))      # 10.0  (average of a number with itself is itself)


# ----------------------------------------------------------------------
# Try it yourself
# ----------------------------------------------------------------------
# 1. Make a box called "age", put your age in it, print it, then overwrite
#    it with next year's age and print again.
# 2. Make two boxes x and y with any numbers. Print average(x, y).
# 3. What does average(x, y) give when x and y are the same? Predict, then check.
