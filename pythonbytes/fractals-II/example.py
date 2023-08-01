from turtle import Turtle
import math

t = Turtle(); t.speed(1000); t.up()

def csquare(z): return (z[0]*z[0]-z[1]*z[1], 2.*z[0]*z[1])

def add(a, b): return (a[0]+b[0], a[1]+b[1])
    
def z_squared_plus_c_n_times(z, c, n):
    if n == 0: return z
    nprime, zprime = n - 1, add(csquare(z), c)
    return z_squared_plus_c_n_times(zprime, c, nprime)
    
def cratio(z, c, n):
    zp = z_squared_plus_c_n_times(z, c, n)
    mzp = math.sqrt(zp[0]*zp[0] + zp[1]*zp[1])
    mz = math.sqrt(z[0]*z[0] + z[1]*z[1])
    return mz/mzp

def dotcolor(z, c, n):
    rat = cratio(z, c, n)
    if rat < 0.2: return 'black'
    elif rat < 0.4: return 'blue'
    elif rat < 0.6: return 'green'
    elif rat < 0.8: return 'yellow'
    elif rat < 1.0: return 'orange'
    elif rat < 1.2: return 'red'
    else: return 'white'


i0, iN, di = -200, 201, 1     # used in the coordinate loop
j0, jN, dj = -200, 201, 1
xF = 1.2/math.fabs(i0)        # converting integer coordinate to float small coordinate
yF = 1.2/math.fabs(j0)

c = (0.3, -0.4) # The constant added to z-squared

for i in range(i0, iN, di):
    x = i * yF
    for j in range(j0, jN, dj):
        y = j*yF
        thisColor = dotcolor((x, y), c, 8)
        if thisColor != 'black':
            t.setposition(i, j)
            t.dot(1, thisColor)
        
