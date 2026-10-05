from mcpi.minecraft import Minecraft
import numpy as np
from random import randint

x0 = 1000
z0 = 1900

# This is poor form: It treats a as a minecraft position and b as a tuple of 3 coordinates
def FracJump(a, b, frac): return (a.x + frac*(b[0]-a.x), a.y + frac*(b[1]-a.y), a.z + frac*(b[2]-a.z))

# Chaos game in 3D is len(v) vertices and frac jumps; we will do nSteps of these
#   mc is minecraft; notice the root position is determined by the player; it is not passed
#   v is a list of triples, vertex relative coordinates in (x, y, z)
#     notice there are n = len(v) such vertices, implicit
#     suppose we are at location p and select vertex q to move towards
#   frac is the distance we move along pq: And this might be more than 1 or negative
#   nSteps is the number of hops we will take
#   block and blockQ specify the artifact at p
def ChaosGame3D(mc, v, frac, nHops, block, blockQ): 
    n, a = len(v), mc.player.getPos()
    a.x, a.y, a.z = a.x + 20, 20, a.z + 20            # an origin offset from player
    p = mc.player.getPos()      
    verts = []                      # vertex locations as triples
    for i in range(n):
        (p.x, p.y, p.z)= (v[i][0] + a.x, v[i][1] + a.y, v[i][2] + a.z)
        verts.append((p.x, p.y, p.z))
    for i in range(nHops):
        p.x, p.y, p.z = FracJump(p, verts[randint(0, n-1)], frac)
        # mc.setBlock(p.x, p.y, p.z, randint(1,60), 0)
        mc.setBlock(p.x, p.y, p.z, block)

mc = Minecraft.create()
mc.player.setPos(x0, 100, z0)      # Put the player at this location

v = []
# for i in range(n): v.append((randint(0,511),randint(0,255),randint(0,511)))
v.append((0, 0, 0))
v.append((180, 0, 300))
v.append((-180, 0, 300))
v.append((0, 255, 180))

ChaosGame3D(mc, v, frac = 0.5, nHops = 5000, block = 41, blockQ = 0)
