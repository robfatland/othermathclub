import sys

# This could use the n 2n rule and other ideas about primes
# Reinstate p[] to use only those as candidate multipliers for new composites?...
# ...no that won't work beyond a certain point: You don't know them yet

def NthPrime(nth):
    if nth == 1: print('first prime is 2'); return 2
    if nth == 2: print('second prime is 3'); return 3

    # p = [2, 3]      # list of primes is not necessary with a sieve
    n = 2             # n is how many primes found so far
    c = []            # list of composites
    lp = 3            # lp is short for 'last prime' (largest so far)
                      #   lp starts out as 3
    while n < nth:
        # Go through all of the odd multipliers of the current prime
        #   Even multipliers will never be checked because they are
        #   automatically composite.
        endpoint = int(1000000/lp)
        for i in range(lp, endpoint, 2): c.append(lp*i)
            # lc = lp*i                     # 'largest composite'
            # c.append(lp*i)
            # the next line makes it incredibly slow
            # if not lc in c: c.append(lc)  # sieve approach
            # if i > 1000: print(i, lp, endpoint, lc, len(c))
        for j in range(lp+2, 1000000, 2):
            if not j in c:
                lp = j
                # p.append(lp)
                n = n+1
                break
    return lp

# There are 78,498 primes less than one million
nth = int(input('Enter which prime you want: '))
if nth > 78498:
    print('Sorry this program only handles up to the 78498th prime...')
    sys.exit()

nthprime = NthPrime(nth)    
print('prime ', nth, ' = ', nthprime)




        
        
