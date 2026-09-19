print('This program figures out where Ms. Halfway winds up')

d = 1.        # Destination d is the post office (1.)
m = 0.        # Her location m begins at home (0.)
s = 0.        # Start s at home (0.)

print('At the start here are variables m, s, d:')
print(m, s, d)
print()

journeys = 4    # How many halfway journeys to make

for j in range(journeys): # for-loop over journeys
    m = (d + s) / 2.      # average start s and destination d
    d = s                 # next destination d is
                          #     where she just left from (s)
    s = m                 # update new start location s
    print(m, s, d)

print('At the end Ms Halfway is at:')
print(m)
