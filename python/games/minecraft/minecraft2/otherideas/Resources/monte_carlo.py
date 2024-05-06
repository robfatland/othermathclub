from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time
import sys
import kilroy
# from kilroy import msg

def FracJump(a, b, frac):
    retX = a.x + frac*(b.x-a.x)
    retY = a.y + frac*(b.y-a.y)
    retZ = a.z + frac*(b.z-a.z)
    return (retX, retY, retZ)

def MonteCarlo(mc, origin, v, frac, nSteps, eraseAll):   

    thisPos = mc.player.getPos()
    thisPos.x = origin.x + 17
    thisPos.y = origin.y + 24
    thisPos.z = origin.z + 7

    nVerts = len(v)

    vertices = []
    for i in range(nVerts):
        aPos = mc.player.getPos()
        aPos.x = v[i][0] + origin.x
        aPos.y = v[i][1] + origin.y
        aPos.z = v[i][2] + origin.z
        vertices.append(aPos)
            
    for i in range(nSteps):
        thisPos.x, thisPos.y, thisPos.z = FracJump(thisPos, vertices[r.randint(0, nVerts-1)], frac)
        mc.setBlock(thisPos.x, thisPos.y, thisPos.z, 14)


mc = Minecraft.create()
xPos, yPos, zPos = 2500, 50, 2500       
mc.player.setPos(xPos, yPos, zPos)

originPos=mc.player.getPos()

originPos.x += 0
originPos.y -= 2

# msg(mc, "start tetrahedron")
tasks = [False, True]

# minecraft, LLH corner of the lower west hall, [floors, vertices, edges], material, bool erase
v = []
v.append((0,0,0))
v.append((200,0,150))
v.append((200,0,-150))
v.append((120,205,0))
nSteps = 1000
frac = 0.5
eraseAll = False
MonteCarlo(mc, originPos, v, frac, nSteps, eraseAll)
