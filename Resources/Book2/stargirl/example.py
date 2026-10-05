from random import random
from turtle import Turtle
from math import sqrt
from math import cos
from math import sin
from math import atan2
from math import pi

def d(a, b): return sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

def SetPlanets():
    for i in range(n):
        if i == 0: p.append((0, 0, mass[i], radius[i])) # Jupiter at (0, 0)
        else:
            tryAgain = True
            while tryAgain:
                tryAgain = False
                xm, ym = -pSpace + 2*pSpace*random(), -pSpace + 2*pSpace*random()
                for j in range(i):
                    if d((xm, ym), (p[j][0], p[j][1])) < p[j][3] + radius[i]: tryAgain = True
            p.append((xm, ym, mass[i], radius[i])) # p is a list of tuples (x, y, mass, radius)

def DrawPlanets():
    global s
    for i in range(n): s.up(); s.setpos(p[i][0], p[i][1]-p[i][3]); s.down(); s.circle(p[i][2]*rFactor);

def Crash(x, y):
    global p, n
    for i in range(n): 
        if d((x, y), (p[i][0], p[i][1])) < p[i][3]: return True
    return False
    
aFactor = 2.          # Change the sign of aFactor to try out anti-gravity
outofbounds = 300.    # Makes the switch faster to next spaceship
pSpace = 160.         # Defines the region where the moons may be found
time = 500            # Number of time steps
subtime = 20          # Number of time sub-steps between steps
n = 5                 # Number of planetoids (Jupiter + 4 moons)
rFactor = 2           # Converts mass to planetoid radius

mass = [10., 0.3, 4.1, 2.6, 3.3]    # masses of the planetoids

radius = [rFactor*i for i in mass]

# This will create the planetoid list p[]
p = []
SetPlanets()

# This will draw the planetoids
s=Turtle(); s.up(); s.speed(0); s.down(); s.dot(1); s.up()
DrawPlanets()
s.hideturtle()

# b is Stargirl's spaceship
b=Turtle(); b.speed(0); b.up(); b.color('red')

# This determines the various arrival locations for the spaceship
y0, yI, ny = 20., 1., 100

# Now we loop over arrival locations
for i in range(ny):
    
    # x and y are Stargirl's location
    x, y = -200., y0 + i*yI
    
    # vx and vy are Stargirl's velocity components along the x- and y-axes
    vx, vy = 0.5/float(subtime), 0.0/float(subtime)
    
    # Place Stargirl's spaceship at her starting point
    b.setpos(x,y)
    b.down()
    
    # The time loop allows Stargirl to move
    for t in range(time):
        
        # The sub-time loop lets some time go by without drawing
        for subt in range(subtime):
            
            # We loop over the planetoids and add in the gravity effects of each
            for j in range(n):
                
                # This is the effect of planetoid j on the velocity (vx, vy)
                distance = d((x, y), (p[j][0],p[j][1]))
                accel = aFactor*p[j][2]/(distance*distance)/float(subtime)
                angle = pi*b.towards(p[j][0], p[j][1])/180.
                vx += accel*cos(angle)
                vy += accel*sin(angle)
                
            # The velocity is now up to date; so let's move position (x, y)
            x = x + vx
            y = y + vy
            
            # If we crashed into a planetoid: break out of the sub-time loop
            if Crash(x, y): break
        
        # Let's extend the trajectory line to our new location and mark it with a dot
        b.setheading((180./pi)*atan2(vy, vx))
        b.setpos(x, y)
        b.dot(1)
        
        # If we have flown far outside the image or crashed: Quit this trajectory
        if x*x + y*y > outofbounds*outofbounds or Crash(x, y): break
    
    # Now before we go start a new trajectory: Pick up the pen
    b.up()       
            
      
    
