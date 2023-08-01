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
        R, v    = Flip(R, nl[rand.randint(0, nn-1)])         # flip randomly; return 
                                                             #   tuple = new R + 2 x abs(negative site) 
        fc     += 1                                          # update flip count
        fs     += v                                          # update flip sum
    return fc, fs

def RPositives(R):    return [i for i in range(len(R)) if R[i]  > 0]
def RNegatives(R):    return [i for i in range(len(R)) if R[i]  < 0]
def RNonpositives(R): return [i for i in range(len(R)) if R[i] <= 0]
def RNonnegatives(R): return [i for i in range(len(R)) if R[i] >= 0]

def ReverseFlip(R, i, n):
    '''Returns R after site i is reverse-flipped'''
    RF = R[:]
    a = RF[i]
    RF[i] = -a
    RF[i-1] += a
    RF[(i+1)%n] += a
    return RF

def Congruent(R1, R2):
    '''R1 congruent R2: The same up to a phase (index) shift'''
    n = len(R2)
    for i in range(n):              # start-compare index of R2
        match = True                # presume this is a match
        for j in range(n):          # run through R1 indices
            R2idx = (i + j) % n     
            if R1[j] != R2[R2idx]: 
                match = False
                break
        if match: return True
    return False

def RingMagnitude(R):
    '''
    returns the maximum absolute value of site values in R
    '''
    n, ringmax = len(R), 0
    for i in range(n):
        if abs(R[i]) > ringmax: ringmax = abs(R[i])
    return ringmax


def IncrementR(R, m, n, idx):
    '''Increment the ring considered as an n-digit base-m integer'''
    if idx < 0: return False
    R[idx] += 1
    if R[idx] > m:
        R[idx] = -m
        return IncrementR(R, m, n, idx-1)
    else: return R



def BmGenerator(m, n):
    '''
    Generate L: A list of possible rings Rn where all sites have abs <= m. Do not retain rings that are 
    cyclic permutations in forward or reverse order of existing Rn in L. 
    '''
    L = []
    R = [-m]*n
    
    while True:
        Rt = R.copy()
        if not sum(Rt) == 1: 
            goodR = False
        elif not (-m in R or m in R):
            goodR = False
        else: 
            goodR = True
            for c in L:               # c is a comparative ring from the existing list
                if Congruent(Rt, c):
                    goodR = False
                    break
                Rt.reverse()
                if Congruent(Rt, c):
                    goodR = False
                    break
        if goodR: L.append(R[:]) 
        R = IncrementR(R, m, n, n-1)
        if not R: return L

