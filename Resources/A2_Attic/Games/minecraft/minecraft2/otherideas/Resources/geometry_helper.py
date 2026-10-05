# geometry_helper contains simple or 'primitive' geometric builders
#
# pos = mc.player.getPos() # to set type (inelegant)

from mcpi.minecraft import Minecraft
import numpy as np
pi = np.pi
def d2r(d): return pi*d/180.0
def r2d(r): return 180.0*r/pi
def swap(a, b): c = b; b = a; a = c; return (a, b)

a = 1
b = 5
a, b = swap(a,b)
print(a, b)

# Create a line of blocks between positions a and b
#   mc is a minecraft object
#   a and b are mc.player.getPos() positions
#   block is a tuple (blockType, blockQualifier)
def LineSegment(mc, a, b, block):
    if a == b: mc.setBlock(a.x, a.y, a.z, block[0], block[1])
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
                mc.setBlock(x,y,z,block[0], block[1])
        elif dy >= dz:
            if a.y > b.y: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.y - a.y), a.x
            mz, nz = (b.z - a.z) / (b.y - a.y), a.z
            for yloc in range(int(a.y),int(b.y)+1):
                y = 1.0*yloc
                yrel = y - a.y
                x, z = mx * yrel + nx, mz * yrel + nz
                mc.setBlock(x,y,z,block[0], block[1])
        else:
            if a.z > b.z: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.z - a.z), a.x
            my, ny = (b.y - a.y) / (b.z - a.z), a.y
            for zloc in range(int(a.z),int(b.z)+1):
                z = 1.0*zloc
                zrel = z - a.z
                x, y = mx * zrel + nx, my * zrel + ny
                mc.setBlock(x,y,z,block[0], block[1])

# Create a line of blocks between positions a and b
#   mc is a minecraft object
#   a and b are mc.player.getPos() positions
#   block is a tuple (blockType, blockQualifier)
def LineSegmentExperimental(mc, a, b, block):
    if a == b: mc.setBlock(a.x, a.y, a.z, block[0], block[1])
    else: 
        dx, dy, dz = np.abs(a.x-b.x), np.abs(a.y-b.y), np.abs(a.z-b.z)
        if dx >= dy and dx >= dz: c0, c1, order = a.x, b.x, (0, 1, 2)
        elif dy >= dz: c0, c1, order = a.y, b.y, (1, 0, 2)
        else: c0, c1, order = a.z, b.z, (2, 0, 1)
        if c0 > c1: c0, c1 = swap(c0, c1)
        for c in range(int(c0), int(c1) + 1):
            # and so on

            
            if a.x > b.x: a, b = swap(a, b)
            my, ny = (b.y - a.y) / (b.x - a.x), a.y  # respective slope / intcpt
            mz, nz = (b.z - a.z) / (b.x - a.x), a.z  # respective slope / intcpt
            for xloc in range(int(a.x),int(b.x)+1):
                x = 1.0*xloc
                xrel = x - a.x
                y, z = my * xrel + ny, mz * xrel + nz
                mc.setBlock(x,y,z,block[0], block[1])
        elif dy >= dx and dy >= dz:
            if a.y > b.y: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.y - a.y), a.x
            mz, nz = (b.z - a.z) / (b.y - a.y), a.z
            for yloc in range(int(a.y),int(b.y)+1):
                y = 1.0*yloc
                yrel = y - a.y
                x, z = mx * yrel + nx, mz * yrel + nz
                mc.setBlock(x,y,z,block[0], block[1])
        else:
            if a.z > b.z: a, b = swap(a, b)
            mx, nx = (b.x - a.x) / (b.z - a.z), a.x
            my, ny = (b.y - a.y) / (b.z - a.z), a.y
            for zloc in range(int(a.z),int(b.z)+1):
                z = 1.0*zloc
                zrel = z - a.z
                x, y = mx * zrel + nx, my * zrel + ny
                mc.setBlock(x,y,z,block[0], block[1])
                
# Draw line segments specified in absolute coordinates
#   mc is the minecraft object
#   x and y are tuples: triple positions remembering y is vertical
#   block is a tuple: (blockType, blockQualfier)
#   Kilroy: initializing a position should be improved
def LineSegmentAbsolute(mc, x, y, block):
    a = mc.player.getPos()
    b = mc.player.getPos()   # b = a fails: a and b are the same thing
    a.x, a.y, a.z = x[0], x[1], x[2]
    b.x, b.y, b.z = y[0], y[1], y[2]
    LineSegment(mc, a, b, block)
    


def Plate(mc, a, b, c, blockType):
    tv = b - a
    mag = np.sqrt(tv.x*tv.x + tv.y*tv.y + tv.z*tv.z)
    tvn = tv
    tvn.x /= mag
    tvn.y /= mag
    tvn.z /= mag
    ab = a
    for i in range(int(mag)+1):
        LineSegment(mc, ab, c, quartz)
        ab += tvn
    mc.postToChat("made a plate")
                  

