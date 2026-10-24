def addemup(x, y):
    return x + y


a = 1
b = 1
c = addemup(a, b)
print(a, b, c)

a = b
b = c
c = addemup(a, b)
print(a, b, c)

for n in range(20):
    a = b
    b = c
    c = addemup(a, b)
    print(a, b, c)




# ----------------------------------------------------------------------
# Stretch goal: the ratio (uncomment to try)
# ----------------------------------------------------------------------
# The numbers grow forever, but b / a settles down. Add this print inside
# the loop above and watch it home in on the golden ratio, ~1.618.
#
#     print(b / a)
