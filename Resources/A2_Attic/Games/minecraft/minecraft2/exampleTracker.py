# This program does not work as intended
#   It is supposed to place blocks up ahead in the direction we are
#   moving but it only does something vaguely like that... needs work


from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import numpy as np
import time
from random import randint

# import cgkit
pi = np.pi
def d2r(d): return pi*d/180.0
def r2d(r): return 180.0*r/pi

def swap(a, b): c = b; b = a; a = c; return (a, b)

# Try this out to get the highest non-air block y value
# y = mc.getHeight(0,0)


mc = Minecraft.create()
p = mc.player.getPos()
v = Vec3(p.x, p.y, p.z)

# I don't think these exist
# print(mc.player.getRotation())
# print(mc.player.getPitch())
# print(mc.player.getDirection())


# This is a useful function but it is not used at this time...
# It creates a straight line of blocks between positions a and b
#   mc is a minecraft object
#   a and b are mc.player.getPos() positions
#   block is a tuple (blockType, blockQualifier)
#   I think 38 is some flowers...
def LineSegment(mc, a, b, block):
    if a == b: mc.setBlock(a.x, a.y, a.z, 38, block[1])
    else: 
        dx, dy, dz = np.abs(a.x-b.x), np.abs(a.y-b.y), np.abs(a.z-b.z)
        if dx >= dy and dx >= dz:
            if a.x > b.x: a, b = swap(a, b)
            my, ny = (b.y - a.y) / (b.x - a.x), a.y  # respective slope / intcpt
            mz, nz = (b.z - a.z) / (b.x - a.x), a.z  # respective slope / intcpt
            for xloc in range(int(a.x),int(b.x)+1):
                x = 1.0*xloc
                xrel = x - a.x
                y, z = my * xrel + ny, mz * xrel + nz
                mc.setBlock(x, y, z, 103, randint(0,8))
        elif dy >= dz:
            if a.y > b.y: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.y - a.y), a.x
            mz, nz = (b.z - a.z) / (b.y - a.y), a.z
            for yloc in range(int(a.y),int(b.y)+1):
                y = 1.0*yloc
                yrel = y - a.y
                x, z = mx * yrel + nx, mz * yrel + nz
                mc.setBlock(x, y, z, 38, randint(0,8))
        else:
            if a.z > b.z: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.z - a.z), a.x
            my, ny = (b.y - a.y) / (b.z - a.z), a.y
            for zloc in range(int(a.z),int(b.z)+1):
                z = 1.0*zloc
                zrel = z - a.z
                x, y = mx * zrel + nx, my * zrel + ny
                mc.setBlock(x, y, z, 38, randint(0,8))

polling_interval = 0.5
ahead_distance = 20.

gold = 41
TNT = 46
redstone = 152
flowers = 38
counter = 0
while True:
    
    time.sleep(polling_interval)
    
    p2 = mc.player.getPos()           # p2 is position 2, the current player position

    counter += 1
    v = p2 - p
    mag_v = np.sqrt(v.x*v.x + v.y*v.y + v.z*v.z)

    # print(v, mag_v)
    
    # Only if the player has moved from the previous fix do we proceed
    if mag_v > 2.:

        # This draws a trailing line
        # LineSegment(mc, p, p2, (49, 0))
        # p = p2

        v.x *= ahead_distance/mag_v
        v.y *= ahead_distance/mag_v
        v.z *= ahead_distance/mag_v

        # cc is 'circle center': a location forward of the player
        cc = p2 + Vec3(v.x, v.y, v.z)

        if counter % 10 == 0:
            # Do not place some dynamite to explode
            # mc.setBlock(cc.x, cc.y-1, cc.z, redstone)
            # mc.setBlock(cc.x, cc.y, cc.z, TNT, 1)
            mc.setBlock(cc.x, cc.y, cc.z, gold)
        else:
            mc.setBlock(cc.x, cc.y, cc.z, flowers, randint(0, 8))

    if counter > 300: break

    p = p2
        

    
