from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time

quartz = 155
air = 0
redstone = 152
TNT = 46
still_water = 9
flowing_water = 8
diamond = 57
flowing_lava = 10
wool = 35
magenta_for_wool = 2
gold = 41
bricks = 45
glass = 95
obsidian = 49
portal = 90

#
# utilities
#

def msg(mc, msg):
    mc.postToChat(msg)
    print(msg)

def mcdistance(a, b): return np.sqrt(float((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) + (a.z-b.z)*(a.z-b.z)))

def norm(x, y, z): return np.sqrt(x*x + y*y + z*z)

# static array of bug locations in a 200 x 200 x 200 cube with +y bias of 55 (up out of the ground)
# use these two lines from the Python command line to genereate random locations
# from random import randint as ri
# xzExtent, yExtent, yOffset = 500, 200, 55
# for i in range(50): print('randomBugs.append((', ri(0,xzExtent), ',', yOffset + ri(0,yExtent), ',', ri(0,xzExtent), '))')
randomBugs = []
randomBugs.append(( 30 , 170 , 490 ))
randomBugs.append(( 317 , 111 , 285 ))
randomBugs.append(( 379 , 242 , 440 ))
randomBugs.append(( 475 , 147 , 112 ))
randomBugs.append(( 461 , 251 , 240 ))
randomBugs.append(( 446 , 145 , 148 ))
randomBugs.append(( 217 , 205 , 106 ))
randomBugs.append(( 176 , 118 , 264 ))
randomBugs.append(( 481 , 236 , 357 ))
randomBugs.append(( 22 , 114 , 196 ))
randomBugs.append(( 207 , 76 , 360 ))
randomBugs.append(( 106 , 103 , 44 ))
randomBugs.append(( 247 , 220 , 353 ))
randomBugs.append(( 83 , 210 , 95 ))
randomBugs.append(( 437 , 240 , 404 ))
randomBugs.append(( 120 , 85 , 56 ))
randomBugs.append(( 401 , 77 , 360 ))
randomBugs.append(( 18 , 91 , 26 ))
randomBugs.append(( 417 , 209 , 265 ))
randomBugs.append(( 22 , 134 , 57 ))
randomBugs.append(( 320 , 85 , 44 ))
randomBugs.append(( 175 , 222 , 349 ))
randomBugs.append(( 417 , 96 , 478 ))
randomBugs.append(( 50 , 102 , 491 ))
randomBugs.append(( 492 , 151 , 421 ))
randomBugs.append(( 367 , 202 , 371 ))
randomBugs.append(( 405 , 109 , 350 ))
randomBugs.append(( 471 , 203 , 369 ))
randomBugs.append(( 467 , 92 , 133 ))
randomBugs.append(( 137 , 102 , 110 ))
randomBugs.append(( 368 , 152 , 424 ))
randomBugs.append(( 263 , 219 , 352 ))
randomBugs.append(( 355 , 68 , 174 ))
randomBugs.append(( 409 , 76 , 214 ))
randomBugs.append(( 442 , 95 , 7 ))
randomBugs.append(( 73 , 242 , 365 ))
randomBugs.append(( 436 , 65 , 281 ))
randomBugs.append(( 167 , 165 , 353 ))
randomBugs.append(( 336 , 71 , 46 ))
randomBugs.append(( 77 , 108 , 499 ))
randomBugs.append(( 63 , 120 , 409 ))
randomBugs.append(( 251 , 134 , 349 ))
randomBugs.append(( 409 , 57 , 54 ))
randomBugs.append(( 208 , 74 , 436 ))
randomBugs.append(( 187 , 89 , 214 ))
randomBugs.append(( 474 , 241 , 485 ))
randomBugs.append(( 361 , 175 , 229 ))
randomBugs.append(( 103 , 189 , 498 ))
randomBugs.append(( 467 , 211 , 258 ))
randomBugs.append(( 267 , 255 , 33 ))

def Platform(mc, pos, a, DX, DY, DZ, blockType):
    for i in range(a):
        for k in range(a):
            mc.setBlock(pos.x + i + DX, pos.y + DY, pos.z + k + DZ, blockType)


def Floor(mc, center, dims, blocks):
    # deal with the floor dimensions
    xF, yF, zF = int(dims[0]), int(dims[1]), int(dims[2])
    yF = 1   # hardcode
    if xF < 9: xF = 9
    if zF < 9: zF = 9
    if xF % 2 == 0: xF = xF + 1
    if zF % 2 == 0: zF = zF + 1
    xH = int(xF / 2)       # so 17 becomes 8
    zH = int(zF / 2)

    # set corner coordinates
    x0 = int(center.x - xH)
    y0 = int(center.y)
    z0 = int(center.z - zH)

    # set materials
    floorBlock = blocks[0]
    floorState = blocks[1]

    for i in range(x0, x0 + xF):
        for j in range(y0, y0+1):
            for k in range(z0, z0 + zF):
                mc.setBlock(i, j, k, floorBlock, floorState)
    return

def SparseSphereShell(mc, pos, radius, step, blockType):
    minrad = radius - 1
    maxrad = radius
    xc = pos.x
    yc = pos.y
    zc = pos.z
    for x in range(int(xc-radius-1), int(xc+radius+2), step):
        for y in range(int(yc-radius-1), int(yc+radius+2), step):
            for z in range(int(zc-radius-1), int(zc+radius+2), step):
                distance = np.sqrt((x-xc)*(x-xc)+(y-yc)*(y-yc)+(z-zc)*(z-zc))
                if distance > minrad and distance < maxrad:
                    mc.setBlock(x, y, z, blockType)

# Kilroy resolve do we have the calling code initialize mc positions? Or do
#   we allow the calling code to pass triples? enumerating coordinates seems wrong.


# For drawing line segments from coordinates rather than from positions
def LineSegmentXYZ(mc, pos, x, y, z, u, v, w, blockType, blockState = 0):
    a = mc.player.getPos()
    b = mc.player.getPos()
    a.x=x
    a.y=y
    a.z=z
    b.x=u
    b.y=v
    b.z=w
    LineSegment(mc, a, b, blockType, blockState)

def Plate(mc, a, b, c, blockType, blockState = 0):
    tv = b - a
    mag = np.sqrt(tv.x*tv.x + tv.y*tv.y + tv.z*tv.z)
    tvn = tv
    tvn.x /= mag
    tvn.y /= mag
    tvn.z /= mag
    ab = a
    for i in range(int(mag)+1):
        LineSegment(mc, ab, c, blockType, blockState)
        ab += tvn


##############
##
## Program: Kaboom
##
##   Creates a set of redstone spherical shells and places dynamite on them... which ought to go off
##
##############
##makeSphere = False
##detonate = False
##somePos=mc.player.getPos() # just sets somePos to be a position-type variable
##somePos.x=6700             # hardcode the location based on earlier sleuthing
##somePos.y=102
##somePos.z=314
##shellRadius = 28
##if makeSphere:
##    SphereShell(mc, somePos, shellRadius, redstone)     # a redstone shell will set off any dynamite set upon it
##if detonate:
##    dynamite_spacing = 3
##    somePosPlus1Y = somePos
##    somePosPlus1Y.y += 1
##    # a sparse shell will place TNT here and there giving a partially destroyed sphere as a result 
##    SparseSphereShell(mc, somePosPlus1Y, shellRadius, dynamite_spacing, TNT)

# create a block bar between a and b (sparse)
def LineSegment(mc, a, b, blockType, blockState=0):
    if a == b:
        mc.setBlock(a.x, a.y, a.z, blockType, blockState)
        return
    dx = np.abs(a.x-b.x)
    dy = np.abs(a.y-b.y)
    dz = np.abs(a.z-b.z)
    if dx >= dy and dx >= dz:
        if a.x > b.x:
            c = b
            b = a
            a = c
        my = (b.y - a.y) / (b.x - a.x)
        ny = a.y
        mz = (b.z - a.z) / (b.x - a.x)
        nz = a.z
        for xloc in range(int(a.x),int(b.x)+1):
            x = 1.0*xloc
            xrel = x - a.x
            y = my * xrel + ny
            z = mz * xrel + nz
            mc.setBlock(x,y,z,blockType, blockState)
            # print(x,y,z)
    elif dy >= dx and dy >= dz:
        if a.y > b.y:
            c = b
            b = a
            a = c
        mx = (b.x - a.x) / (b.y - a.y)
        nx = a.x
        mz = (b.z - a.z) / (b.y - a.y)
        nz = a.z
        for yloc in range(int(a.y),int(b.y)+1):
            y = 1.0*yloc
            yrel = y - a.y
            x = mx * yrel + nx
            z = mz * yrel + nz
            mc.setBlock(x,y,z,blockType, blockState)
            # print(x,y,z)
    else:
        if a.z > b.z:
            c = b
            b = a
            a = c
        mx = (b.x - a.x) / (b.z - a.z)
        nx = a.x
        my = (b.y - a.y) / (b.z - a.z)
        ny = a.y
        for zloc in range(int(a.z),int(b.z)+1):
            z = 1.0*zloc
            zrel = z - a.z
            x = mx * zrel + nx
            y = my * zrel + ny
            mc.setBlock(x,y,z,blockType, blockState)
            # print(x,y,z)
            

# Creates a bar as LineSegment with block type delineated as a list that we map the segment to
def LineSegmentBTList(mc, a, b, blockType):
    if a == b:
        mc.setBlock(a.x, a.y, a.z, blockType[0])
        return
    length = np.sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) + (a.z-b.z)*(a.z-b.z))
    lenBT = len(blockType)
    if lenBT == 0 or length == 0.0: return
    scaleBT = length / float(lenBT)
    dx = np.abs(a.x-b.x)
    dy = np.abs(a.y-b.y)
    dz = np.abs(a.z-b.z)
    if dx >= dy and dx >= dz:
        if a.x > b.x:
            c = b
            b = a
            a = c
        my = (b.y - a.y) / (b.x - a.x)
        ny = a.y
        mz = (b.z - a.z) / (b.x - a.x)
        nz = a.z
        for xloc in range(int(a.x),int(b.x)+1):
            x = 1.0*xloc
            xrel = x - a.x
            y = my * xrel + ny
            z = mz * xrel + nz

            # map to blockType list to set block
            offset = abs(xloc - int(a.x))
            btI = int(float(offset)*scaleBT)
            if btI < 0: btI = 0
            if btI >= lenBT: btI = lenBT - 1
            # mc.setBlock(x,y,z,blockType[btI], magenta_for_wool)
            mc.setBlock(x,y,z,blockType[btI])           
    elif dy >= dx and dy >= dz:
        if a.y > b.y:
            c = b
            b = a
            a = c
        mx = (b.x - a.x) / (b.y - a.y)
        nx = a.x
        mz = (b.z - a.z) / (b.y - a.y)
        nz = a.z
        for yloc in range(int(a.y),int(b.y)+1):
            y = 1.0*yloc
            yrel = y - a.y
            x = mx * yrel + nx
            z = mz * yrel + nz

            # map to blockType list to set block
            offset = abs(yloc - int(a.y))
            btI = int(float(offset)*scaleBT)
            if btI < 0: btI = 0
            if btI >= lenBT: btI = lenBT - 1
            # mc.setBlock(x,y,z,blockType[btI], magenta_for_wool)
            mc.setBlock(x,y,z,blockType[btI])
    else:
        if a.z > b.z:
            c = b
            b = a
            a = c
        mx = (b.x - a.x) / (b.z - a.z)
        nx = a.x
        my = (b.y - a.y) / (b.z - a.z)
        ny = a.y
        for zloc in range(int(a.z),int(b.z)+1):
            z = 1.0*zloc
            zrel = z - a.z
            x = mx * zrel + nx
            y = my * zrel + ny
            # map to blockType list to set block
            offset = abs(zloc - int(a.z))
            btI = int(float(offset)*scaleBT)
            if btI < 0: btI = 0
            if btI >= lenBT: btI = lenBT - 1
            # mc.setBlock(x,y,z,blockType[btI], magenta_for_wool)
            mc.setBlock(x,y,z,blockType[btI])

def Blinker(pos, delay1, delay2, nBlinks, blockType1, blockType2, DX, DY, DZ):
    for i in range(nBlinks):
        time.sleep(delay1)
        mc.setBlock(pos.x + DX, pos.y + DY, pos.z + DZ, blockType1)
        time.sleep(delay2)
        mc.setBlock(pos.x + DX, pos.y + DY, pos.z + DZ, blockType2)


def Tesseract(mc, refPos, d, blockType):

    # pos is a copy of (not a pointer to) refPos
    pos = mc.player.getPos()
    pos.x = refPos.x
    pos.y = refPos.y
    pos.z = refPos.z

    # a and b will be used to designate opposite ends of the beams of the two cuboids
    a = mc.player.getPos()
    b = mc.player.getPos()
    deltaX = (d[0]-d[3])/2
    deltaY = (d[1]-d[4])/2
    deltaZ = (d[2]-d[5])/2

    # outer cuboid
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x + d[0], pos.y, pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y, pos.z, pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y, pos.z, pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[1], pos.z, pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[1], pos.z, pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[2], pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[2], pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)

    pos.x += deltaX
    pos.y += deltaY
    pos.z += deltaZ

    # inner cuboid (this code could merge with the outer cuboid)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x + d[3], pos.y, pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)

    # Eight diagonals
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x - deltaX, pos.y - deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3] + deltaX, pos.y - deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x - deltaX, pos.y + d[4] + deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x - deltaX, pos.y - deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z, pos.x + d[3] + deltaX, pos.y + d[4] + deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z + d[5], pos.x + d[3] + deltaX, pos.y - deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z + d[5], pos.x - deltaX, pos.y + d[4] + deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3] + deltaX, pos.y + d[4] + deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
 
def TesseractPortal(mc, refPos, d, blockType, portalType):
    portal = portalType        # this is 90 for an actual portal; but to make it erasable we stipulate this
    
    # pos is a copy of (not a pointer to) refPos
    pos = mc.player.getPos()
    pos.x = refPos.x
    pos.y = refPos.y
    pos.z = refPos.z

    # a and b will be used to designate opposite ends of the beams of the two cuboids
    a = mc.player.getPos()
    b = mc.player.getPos()
    deltaX = (d[0]-d[3])/2
    deltaY = (d[1]-d[4])/2
    deltaZ = (d[2]-d[5])/2

    # outer cuboid
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x + d[0], pos.y, pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y, pos.z, pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y, pos.z, pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[1], pos.z, pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[1], pos.z, pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[2], pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[2], pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x + d[0], pos.y + d[1], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x + d[0], pos.y, pos.z + d[2]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[0], pos.y + d[1], pos.z + d[2], pos.x, pos.y + d[1], pos.z + d[2]
    LineSegment(mc, a, b, blockType)

    pos.x += deltaX
    pos.y += deltaY
    pos.z += deltaZ

    # inner cuboid (this code could merge with the outer cuboid)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x + d[3], pos.y, pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x, pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3], pos.y + d[4], pos.z
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3], pos.y, pos.z + d[5]
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x, pos.y + d[4], pos.z + d[5]
    LineSegment(mc, a, b, blockType)

    for i in range(int(pos.x+1), int(pos.x + deltaX - 1)):
        a.x, a.y, a.x, b.x, b.y, b.z = i, pos.y + 1, pos.z, i, pos.y + deltaY - 1, pos.z
        LineSegment(mc, a, b, portal, 1)
        a.x, a.y, a.z, b.x, b.y, b.z = i, pos.y + 1, pos.z, i, pos.y + deltaY - 1, pos.z
        LineSegment(mc, a, b, portal, 1)
    for k in range(int(pos.z+1), int(pos.z + deltaZ - 1)):
        a.x, a.y, a.x, b.x, b.y, b.z = pos.x, pos.y + 1, k, pos.x, pos.y + deltaY - 1, k
        LineSegment(mc, a, b, portal, 0)
        a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + 1, k, pos.x, pos.y + deltaY - 1, k
        LineSegmentWithState(mc, a, b, portal, 0)

    # Eight diagonals
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z, pos.x - deltaX, pos.y - deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z, pos.x + d[3] + deltaX, pos.y - deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z, pos.x - deltaX, pos.y + d[4] + deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y, pos.z + d[5], pos.x - deltaX, pos.y - deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z, pos.x + d[3] + deltaX, pos.y + d[4] + deltaY, pos.z - deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y, pos.z + d[5], pos.x + d[3] + deltaX, pos.y - deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x, pos.y + d[4], pos.z + d[5], pos.x - deltaX, pos.y + d[4] + deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
    a.x, a.y, a.z, b.x, b.y, b.z = pos.x + d[3], pos.y + d[4], pos.z + d[5], pos.x + d[3] + deltaX, pos.y + d[4] + deltaY, pos.z + d[5] + deltaZ
    LineSegment(mc, a, b, blockType)
