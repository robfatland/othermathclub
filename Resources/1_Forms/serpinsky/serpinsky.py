# support for various serpinsky gasket approaches

from matplotlib import pyplot as plt
from math import sin, cos, tan, sqrt, fabs, pi

def RuleS(s):
    '''
    Apply the x y + - basic substitution rule to string s
    '''
    n = ''
    for c in s:
        if   c == 'x': n += 'y+x+y'
        elif c == 'y': n += 'x-y-x'
        else:          n += c
    return n


def IterateRuleS(s, n):
    '''Apply the x y + - basic substitution rule n times'''
    for i in range(n): s = RuleS(s)
    return s


def A(a):
    while a < 0: a += 360.
    while a >= 360: a -= 360.
    return a

def PlusLeft(alpha): return A(alpha + 60.)

def MinusRight(alpha): return A(alpha - 60.)

def ChartS(s, d):
    '''Create a matplotlib drawing / interpretation of string x'''
    xp, yp = 0., 0.
    x, y = [xp], [yp]
    rtot = sqrt(3)/2
    cfs = [1., .5, -.5, -1., -.5, .5]
    sfs = [0., rtot, rtot, 0., -rtot, -rtot]
    dx = {0.: d*cfs[0], 60.: d*cfs[1], 120.: d*cfs[2], 180.:d*cfs[3], 240.:d*cfs[4], 300.:d*cfs[5]}
    dy = {0.: d*sfs[0], 60.: d*sfs[1], 120.: d*sfs[2], 180.:d*sfs[3], 240.:d*sfs[4], 300.:d*sfs[5]}
    theta = 0.
    for c in s:
        if   c == '+': theta = PlusLeft(theta)
        elif c == '-': theta = MinusRight(theta)
        xp += dx[theta]
        yp += dy[theta]
        x.append(xp)
        y.append(yp)
    fig, ax = plt.subplots(figsize=(12,12))
    ax.plot(x, y)
    return 0


'''
from turtle import Turtle, tracer, update
t = Turtle()
t.hideturtle()
t.speed(0)
tracer(0,0)
for c in s:
  if   c == '+': 
    t.left(60)
  elif c == '-': 
    t.right(60)
  t.forward(4)
update()
'''