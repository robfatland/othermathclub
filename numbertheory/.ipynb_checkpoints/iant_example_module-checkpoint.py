# utility functions
#   bool even, odd, divides
#   factor() -> integer list

from math import sqrt, prod, log2, floor

def even(a): return False if a%2 else True

def odd(a): return True if a%2 else False

def divides(a, b): return not b % a

def prime(n):
    '''Boolean is n prime'''
    if not n%2: return False
    for i in range(3, int(sqrt(n)) + 1, 2): 
        if not n%i: return False
    return True

def is_prime(n): return(prime(n))

def IsPrime(n): return(prime(n))

def factor(n):
    '''sorted list of factors i.e. with repetitions: 8 > [2, 2, 2]'''
    if n < 1:  return('something has gone horribly wrong')
    if n == 1: return [1]
    n_redux = n
    f, d, u = [], 2, int(sqrt(n_redux))
    while True:                                # ...continue til possible divisors exhausted
        while not n_redux % d:                 # ...all factors of value d
            f.append(d)
            n_redux = n_redux // d             # balance of original n remaining
        d = 3 if d == 2 else d + 2             # check 2 and odd numbers up to floor sqrt (n)
        if d > u: break                        # end of outer while
    if n_redux > 1: f.append(n_redux)          # include any residual > 1
    return f

# print(divides(4,9))
# print(factor(31*37*3))



def exponentfactors(n):
    '''n assumed > 1; return (prime, exponent) tuples'''
    if n < 1: print('something has gone dreadfully wrong')
    if n == 1: return [(1, 1)]
    f = sorted(factor(n))
    p, ptr = [(f[0], 1)], 0         # p begins as first factor raised to the 1
    for i in f[1:]:                 # this loop will run if n is composite; 2nd factor onward
        if i == p[ptr][0]: p[ptr] = (i, p[ptr][1] + 1)       # immutable tuple construct
        else:              p.append((i, 1)); ptr += 1        # moving on to a new prime
    return(p)


def uniqueprimefactors(n):
    '''n presumed > 1: Return a list of unique prime factors of n > 1'''
    if n < 1: return('something has gone horribly wrong')
    if n == 1: return [1]
    f, d, u = [], 2, int(sqrt(n))
    while True:
        while not n % d:
            if not d in f: f.append(d)
            n = n // d
        d = 3 if d == 2 else d + 2             # lazy: just check 2 and odds
        if d > u: break
    if n > 1 and not n in f: f.append(n)
    return f

def uniquefactors(n): return uniqueprimefactors(n)

        
def gcd(a, b):
    '''greatest common divisor of a and b both >= 1'''
    if a < 1 or b < 1: return('something has gone terribly wrong')
    af, bf, g = factor(a), factor(b), 1
    for f in af:
        if f in bf: bf.remove(f); g *= f
    return g


def relativelyprime(a, b):
    '''are a and b relatively prime?'''
    return True if gcd(a, b) == 1 else False

def relprime(a, b): return relativelyprime(a, b)

def is_relativelyprime(a, b): return relativelyprime(a, b)

def is_relprime(a, b): return relativelyprime(a, b)

def listproduct(l):
    '''product of all elements of list l: uses built-in math function'''
    return prod(l)


def divisors(n):
    '''list of all the divisors of n including 1 and n'''
    if n < 1: return
    d, f = [1], factor(n)                      # factor() is the list of primes with repetitions
    nf = len(f)                                # 60 will have nf = 4: [2, 2, 3, 5]
    for i in range(1, 2**nf):                  #   binomial theorem
        k = boolkey(i)                         # convert i to a binary list of booleans
        this_list = [1]                        # this_list will be a compiled list of factors from f[]
        for j in range(len(k)):                # scan through the boolean list k
            if k[j]: this_list.append(f[j])    #   ...appending factors from True values
        d.append(prod(this_list))              # append to the result this list-product
    return sorted(list(set(d)))


def divisors_less_n(n):
    '''list of all the divisors of n except n'''
    if n < 1: return
    d, f = [1], factor(n)                      # factor() is the list of primes with repetitions
    nf = len(f)                                # 60 will have nf = 4: [2, 2, 3, 5]
    for i in range(1, 2**nf):                  #   binomial theorem
        k = boolkey(i)                         # convert i to a binary list of booleans
        this_list = [1]                        # this_list will be a compiled list of factors from f[]
        for j in range(len(k)):                # scan through the boolean list k
            if k[j]: this_list.append(f[j])    #   ...appending factors from True values
        d.append(prod(this_list))              # append to the result this list-product
    almost_done = sorted(list(set(d)))
    del(almost_done[-1])
    return(almost_done)


def boolkey(n):
    '''return list of bool values of n in binary'''
    key = [False]*(int(log2(n))+1)
    while n > 0:
        p = int(log2(n))
        key[p] = True
        n -= 2**p
    return key


def Totient(n):
    '''Euler's totient(n) = how many relatively prime numbers rp there are for 1 <= r < n'''
    if n < 1: return
    totient = 1
    for i in range(2, n):
        if relativelyprime(n, i): totient += 1
    return totient


def GeneralizedTotient(k, n):
    '''
    Euler's (basic idea) totient: Number of relative primes less than n.
    Generalized: exponent k added i.e. sum the k'th power of all the 
      relative primes of n.
    '''
    if n < 1: return -1
    gtotient = 1
    for i in range(2, n):    # Only active for n > 2 notice
        if relativelyprime(n, i): gtotient += i**k
    return gtotient


def Mobius(n):
    '''mu(1) = 1. mu(n>1) = 0 or (-1)**k; see ANT chapter 2'''
    if n < 1: return
    if n == 1: return 1
    p = exponentfactors(n)
    for i in p: 
        if i[1] > 1: return 0
    return int((-1)**len(p))


def TotientMobiusProduct(n):
    return Totient(n)*Mobius(n)


def Nu(n):
    if n < 1:  print('something has gone horribly wrong')
    if n == 1: return 0
    return len(uniquefactors(n))

#
# Dirichlet convolution section
#   (f, g, n) works directly off the definition for f * g
#   ..."using lists" presumes f and g are lists of values for 1, 2, ..., n
#   ...then there are some aliases
#   ...then across lists produces a list of D-products for n = 1, 2, ..., given n
# 
def Dirichlet(f, g, n):
    '''
    Dirichlet multiplication of two functions f and g for value n
    '''
    if n == 1: return f(1)*g(1)
    total = 0
    for d in divisors(n): total += f(d) * g(n//d)
    return total


def DirichletUsingLists(f, g, n):
    '''
    f and g are lists of function values rather than function names.
    The list index corresponds to n ([0] is extraneous)
    '''
    if n == 1: return(f[1]*f[1])
    total = 0
    for d in divisors(n): total += f[d] * g[n//d]
    return total

def DirichletFromList(f, g, n): return DirichletUsingLists(f, g, n)

def DirichletFromLists(f, g, n): return DirichletUsingLists(f, g, n)

def DirichletAcrossLists(f, g):
    '''
    f and g are lists of function values with index corresponding to n
    This function scans the entire range and returns a list of Dirichlet products
    '''
    DirProds = [0]
    start_n = 1
    end_n = min(len(f), len(g))
    if end_n >= 1:
        for n in range(start_n, end_n): 
            DirProds.append(DirichletUsingLists(f, g, n))
    return(DirProds)

def I(n):
    if n < 1: return 'not arithmetic'
    if n == 1: return 1
    return 0

def U(n):
    return 1

def N(n):
    return n

def Na(n, a):
    return n**a