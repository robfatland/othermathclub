import random as rand
from random import randint, choice

def R_n_zero(n, x):
    '''returns a zero-sum ring with most values between -x and x inclusive'''
    p = [randint(-x, x) for i in range(n-1)]
    p.append(-sum(p))
    return p

def R_n(n, x):
    '''returns a ring with most or all values between -x and x inclusive'''
    p = [randint(-x, x) for i in range(n-1)]
    p.append(1 - sum(p))
    return p

def kJustify(k, n):
    '''ensure k is on [0, n-1]'''
    while k < 0: k += n
    while k >= n: k -= n
    return k

def kDec(k, n):
    '''safely decrement k'''
    kmo = k - 1
    while kmo < 0: kmo += n
    return kmo

def kInc(k, n):
    '''safely increment k'''
    kpo = k + 1
    while kpo >= n: kpo -= n
    return kpo

def Distance(a, b, n):
    '''shorter distance between a and b'''
    return min(abs(a - b), abs((a + n) - b), abs((a - n) - b))

def NegList(R):
    '''return how many negative-valued sites, list of indices'''
    neglocs, nNeg, n = [], 0, len(R)
    for i in range(n):
        if R[i] < 0: neglocs.append(i); nNeg += 1
    return nNeg, neglocs

def PosList(R):
    '''return how many positive-valued sites, list of indices'''
    poslocs, nPos, n = [], 0, len(R)
    for i in range(n):
        if R[i] > 0: poslocs.append(i); nPos += 1
    return nPos, poslocs

def Flip(R, a):
    '''flip site a in R; return R and flip 'double' value'''
    n = len(R)
    if a >= 0 and a < n:
        v = -R[a]
        if v > 0:
            R[a] = v
            R[kDec(a, n)] -= v
            R[kInc(a, n)] -= v
    return R, 2*v

def IsQuiescent(R):
    '''Specific to sum = 1 version'''
    n, Rsum = len(R), 0
    for i in range(n):
        if R[i] < 0: return False
        Rsum += R[i]
    if not Rsum == 1: return False
    return True

def Q(R):
    '''generalized to no negative values in R'''
    for i in range(len(R)):
        if R[i] < 0: return False
    return True

def Entropy(R):
    '''return (predicted) sum of flips to reach Q from R'''
    n, E = len(R), 0
    for i in range(n-1):
        for j in range(i+1, n): E += R[i]*R[j]*(j-i)*(j-i-n)
    return E

def Entropy2(R):
    """
    E = triangle + final vertical (j = n - 1). Does s2 save the day?
    """
    n, s1, s2 = len(R), 0, 0
    for i in range(n-2):                                    
        for j in range(i+1, n-1): s1 += R[i]*R[j]*(j - i)*((j - i) - n) 
    j = n - 1
    for i in range(n-1): s2 += R[i]*R[j]*(j - i)*((j - i) - n) 
    return s1, s2, s1 + s2

def RQ(R, verbose=False):
    '''resolve a ring R to quiescent Q'''
    fc, fs = 0, 0                                            # reset flip count and sum
    while not IsQuiescent(R):                                # Given R this while drives it to Q
        if verbose: print(Entropy(R), R)       
        nn, nl  = NegList(R)                                 # number and list of negative sites
        R, v    = Flip(R, nl[rand.randint(0, nn-1)])         # flip randomly; return tuple = new R + 2 x abs(negative site) 
        fc     += 1                                          # update flip count
        fs     += v                                          # update flip sum
    return fc, fs


# sourceA is a list of rings, each ring being a list of integers
sourceA = [\
          [-1, 2, 0, 0, 0], [-1, 0, 2, 0, 0], 
          [-1, 2, 0, 0, 0, 0], [-1, 0, 2, 0, 0, 0], [-1, 0, 0, 2, 0, 0], \
          [-1, 2, 0, 0, 0, 0, 0], [-1, 0, 2, 0, 0, 0, 0], [-1, 0, 0, 2, 0, 0, 0], \
          [-1, 2, 0, 0, 0, 0, 0, 0], [-1, 0, 2, 0, 0, 0, 0, 0], [-1, 0, 0, 2, 0, 0, 0, 0], [-1, 0, 0, 0, 2, 0, 0, 0], \
          [-1, 2, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 2, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 2, 0, 0, 0, 0, 0],
          [-1, 0, 0, 0, 2, 0, 0, 0, 0],
          [-1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 2, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 0, 2, 0, 0, 0, 0, 0],
          [-1, 0, 0, 0, 0, 2, 0, 0, 0, 0],
          [-1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
          [-1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0], 
          [-1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]
         ]

# These source rings compare binary values and separations for n = 12
sourceB = [\
          [-1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], 
          [-1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
          [-2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0], 
          [-2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0], 
          [-2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
          [-3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0], 
          [-3, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0], 
          [-3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
          [-4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-4, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0], 
          [-4, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0], 
          [-4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0], 
          [-4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
         ]