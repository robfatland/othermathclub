# The Mental Memory Model (MMM): computer memory is boxes
# ...or if you like, drawers ...or if you like, buckets
# Each box has a label: The name of the variable
# Each box has a value
# Each box has a type... more on this later


score = 10          # score is the label, 10 is the value, type is integer
print(score)


score = 25
print(score)


a = 4
b = 10
print(a)
print(b)


total = a + b
print(total)


# this code is our first exception: It does not run!
def average(first, second):
    return (first + second) / 2


midpoint = average(0, 1)
print(midpoint)


ave1 = average(4, 8)
ave2 = average(3, 5)


print(ave1)
print(ave2)


# 1. Make a box called "age", put your age in it, print it, then overwrite
#    it with next year's age and print again.
# 2. Make two boxes x and y with any numbers. Print average(x, y).
# 3. What does average(x, y) give when x and y are the same? Predict, then check.
