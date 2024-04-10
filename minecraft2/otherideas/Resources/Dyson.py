# Dyson creates a spherical shell

clearTheAir = False
clearIncludesPlatform = False
buildPlatform = False
buildMote = False
buildTowers = False
buildTurrets = False
buildBoxes = False
airInside = False
roof = False
seashell = False
groundzero = True

from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time

pi = np.pi
def d2r(d): return pi*d/180.0
def r2d(r): return 180.0*r/pi

mc = Minecraft.create()

# block types:
#   0      air
# 155      quartz
# 152      redstone
#  12      sand
#  46      TNT
#  10      flowing lava
#  35      wool
#      2   magenta qualifier on wool

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


def SphereShell(mc,pos,radius,blockType):
    minrad = radius - 1
    maxrad = radius
    xc = pos.x
    yc = pos.y
    zc = pos.z
    for x in range(int(xc-radius-1), int(xc+radius+2)):
        for y in range(int(yc-radius-1), int(yc+radius+2)):
            for z in range(int(zc-radius-1), int(zc+radius+2)):
                distance = np.sqrt((x-xc)*(x-xc)+(y-yc)*(y-yc)+(z-zc)*(z-zc))
                if distance > minrad and distance < maxrad:
                    mc.setBlock(x,y,z,blockType)

def SparseSphereShell(mc,pos,radius,step,blockType):
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
                    mc.setBlock(x,y,z,blockType)

# For drawing line segments from coordinates rather than from positions
#   Kilroy should figure out how to initialize a position in a more sensible manner
def LineSegmentXYZ(mc, x, y, z, u, v, w, blockType):
    a = mc.player.getPos()
    b = mc.player.getPos()   # b = a does not work; pointer thing I think
    a.x=x
    a.y=y
    a.z=z
    b.x=u
    b.y=v
    b.z=w
    LineSegment(mc, a, b, blockType)
    


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
                  
def RandomNearby(mc, scale):
    pos = mc.player.getPos()
    pos.x += scale + 2.*scale*r.random()
    pos.y += 2.*scale*r.random()
    pos.z += -2.*scale + 4.*scale*r.random()
    return pos

#############
##
## Program: Get a nearby fixed location
##
##   Uses the player position to get a reference location and display axis directions (+z quartz, +x redstone)
##
#############
##mypos = mc.player.getPos()
##print (mypos, mypos.x, mypos.y, mypos.z)
##mc.setBlock(mypos.x, mypos.y, mypos.z+20, quartz)
##mc.setBlock(mypos.x+20, mypos.y, mypos.z, redstone)


##############
##
## Program: Kaboom
##
##   Creates a set of redstone spherical shells and places dynamite on them... which ought to go off
##
##############
makeSphere = False
detonate = False
somePos=mc.player.getPos() # just sets somePos to be a position-type variable
somePos.x=6700             # hardcode the location based on earlier sleuthing
somePos.y=102
somePos.z=314
shellRadius = 28
if makeSphere:
    SphereShell(mc, somePos, shellRadius, redstone)     # a redstone shell will set off any dynamite set upon it
if detonate:
    dynamite_spacing = 3
    somePosPlus1Y = somePos
    somePosPlus1Y.y += 1
    # a sparse shell will place TNT here and there giving a partially destroyed sphere as a result 
    SparseSphereShell(mc, somePosPlus1Y, shellRadius, dynamite_spacing, TNT)

##############
##
## Program: Plates
##
##   Creates a set of triangular plates and some redstone spherical shells
##
##############
# for i in range(3):
#     Plate(mc, RandomNearby(mc, 40), RandomNearby(mc, 40), RandomNearby(mc, 40), quartz)
#     SphereShell(mc, RandomNearby(mc, 40), 30, redstone)



##############
##
## Program: Sick Borg
##
##    Creates a massive cubical Borg ship of random blocks that immediately leaks both water
##    and lava!
##
##############
## Clock to check latency on simple setBlock rendering
# p = RandomNearby(mc, 10)  # p is the position of the binary block; this will toggle
##p = mc.player.getPos()
##state = True
##
##for i in range(20):
##    for j in range(20):
##        for k in range(20):
##
##            mc.setBlock(p.x+i, p.y+j, p.z+k+10, r.randint(0,255))
##            
##            if state:
##                mc.setBlock(p.x, p.y, p.z, quartz)
##                state = False
##                print('quartz')
##                # time.sleep(1)
##            else:
##                mc.setBlock(p.x, p.y, p.z, air)
##                state = True
##                print('air')
##                # time.sleep(1)
                

##############
##
## Program: 3D Graph
##
##   Creates a set of small spheres connected with bars
##
##############
# firstTime = True
# lastPos = mc.player.getPos()
# bagScale = 60.
##for i in range(30):
##    pos = mc.player.getPos()
##    pos.x += bagScale + 2.*bagScale*r.random()
##    pos.y += 2.*bagScale*r.random()
##    pos.z += -2.*bagScale + 4.*bagScale*r.random()
##    SphereShell(mc, pos, 4, 138)
##    if firstTime:
##        firstTime = False
##    else:
##        LineSegment(mc,lastPos,pos,155)
##        lastPos = pos


##p = mc.player.getPos()
##state = True
##
##xSize = 13
##ySize = 13
##zSize = 13
##xMid = 6
##yMid = 6
##zMid = 6
##
##for i in range(xSize):
##    print (i)
##    for j in range(ySize):
##        print(j)
##        for k in range(zSize):
##
##            ix = p.x - i + xMid
##            jy = p.y - j + yMid
##            kz = p.x - k + zMid
##            mc.setBlock(ix, jy, kz, redstone)
            


# create a block bar between a and b (sparse)
def LineSegment(mc, a, b, blockType):
    if a == b:
        mc.setBlock(a.x, a.y, a.z, blockType)
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
            mc.setBlock(x,y,z,blockType)
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
            mc.setBlock(x,y,z,blockType)
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
            mc.setBlock(x,y,z,blockType)

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
            



     
##############
##
## Program: Castle
##
##   You thought McMansions were bad...
##
##############

c=mc.player.getPos() # to set type (inelegant)

## important control parameters
a=121
tower_minradius = 6
tower_maxradius = 14
ntowers = 8
nturrets = 4
nboxes=6
##c.x=6200             # hardcode the location based on earlier sleuthing
##c.y=35
##c.z=440

# ensure these things are integers
c.x = int(c.x)
c.y = int(c.y)
c.z = int(c.z)

ynegoffset = 3
yposoffset = 90

ymin = c.y-ynegoffset
ymax = c.y+yposoffset
yrange = ynegoffset + yposoffset + 1
towerymin=40
towerymax=yposoffset
towerbottommin = 10
towerbottommax = 20
tower_topfloor_takebacky = 4

a2=int(a/2)
b=a-14
b2=int(b/2)



platformMaterial = quartz
moteMaterial = still_water
towerMaterial = diamond
boxMaterial = quartz
turretMaterial= quartz

# Seashell() generates a shell out of blockType material by rotating and translating a triangle
#   This triangle has an axial side and two distal sides: The side from the apex and the side from the terminus.
#   Let's call these respectively distal sides B and C. Axial side is A. Apical is B and mantle opening is C.
#     Call the vertex between A and B 'aa'; then 'bb' and 'cc' going around. With growth we move in the +x direction
#     so that 'aa' gets increasingly positive based on the axialRate and 'cc' gets increasingly positive faster
#     because of the growth scaling.
#   To clarify: The origin is the apex where vertex aa begins; and it moves in the +x direction at the axial rate.
#     Further along the +x axis is vertex cc which moves away from aa at the growth scaling rate (in addition to moving
#     at the axial rate). bb is the off-axis vertex that will spiral around. Side A is Axial between aa and cc. Side B
#     goes from aa to bb, the apex spiral; and side C goes from bb to cc, the mantle spiral.
#   Here are test values and vars...
#     mc:  the minecraft object
#     pos: The apical position
#     3 nWhorls: How many rotations around the axis
#     isSinistral: a bool for left-handed chirality
#     30.0 startScale: Starting axial side of the triangle
#     300.0 endScale: Ending axial side of the triangle
#     10.0 axialRate: How fast the axial side of the triangle moves in the axial direction (units per 2pi of whorl)
#     includeAxis: bool for drawing the axial component of the triangle
#     60.0 apicalAngleDeg: In degrees: angle AB
#     30.0 distalAngleDeg: In degrees: angle AC
#     blockType: What to use
#   We begin oriented along the x axis.
# Ok I made a mistake which created an interesting surface and x = 6800, z = 750. So I copy paste that and comment it out...
# And at x = 8100 z = 850 or so is the first correct one of these; with tpw 100, 3 whorls, 30 to 300 scale, axial rate 10,
#   apical angle 60 deg, mantle angle 30 deg. The only crit is that later triangles grow through prior whorls which is not
#   true to actual shells. Also this procedure should be checked against the log spiral idea.
#
# Minecraft f keys
#   f1 toggles the inventory display
#   f3 toggles the HUD
#   f5 cycles through POVs
#   f11 toggles normal / full-screen
#
def Seashell(mc, pos, nWhorls, isSinistral, startScale, endScale, axialRate, includeAxis, apicalAngleDeg, distalAngleDeg, blockType):
    chirality = 1.0
    if isSinistral: chirality = -1.0
    drawAxial = False
    drawApical = True
    drawMantle = True
    tpw = 520                   # integer ticks per whorl
    origin = mc.player.getPos() # makes origin have type pos, initially at point aa
    origin.x = pos.x
    origin.y = pos.y
    origin.z = pos.z            # makes origin be at the passed location
    aa = mc.player.getPos() # point of connection sides A and B
    aa.x = pos.x
    aa.y = pos.y
    aa.z = pos.z
    bb = mc.player.getPos() # sides B and C
    cc = mc.player.getPos() # sides C and A
    dtr = np.arccos(-1.0)/180.0
    
    geomScale = (endScale - startScale)/(float(tpw*nWhorls))
    dualTanDenom = 1.0/np.tan(apicalAngleDeg*dtr) + 1.0/np.tan(distalAngleDeg*dtr)
    alphaTanDenom = np.tan(apicalAngleDeg*dtr)

    # r30[] will be a list of cell values in a 1D CA
    # in what follows note the 'lg' in the variable names. This refers to the 'largest' that the generating triangle gets
    r30_lg_i = nWhorls*tpw      # tpw is ticks per whorl (angular; so 360 = 1 deg increments). This value is the end size index.
    r30_lg_A = geomScale * float(r30_lg_i) + startScale    # end length of side A (axial)
    r30_lg_r = r30_lg_A / dualTanDenom                     # end height of the generating triangle
    r30_lg_x = r30_lg_r / alphaTanDenom                    # end distance from apical vertex aa to the axial sub-point of vertex bb
    r30_lg_B = np.sqrt(r30_lg_x*r30_lg_x + r30_lg_r*r30_lg_r)   # length of apical side of the triangle from aa to bb
    r30_lg_X = r30_lg_A - r30_lg_x                              # distance from distal vertex cc to axial sub-point of vertex bb
    r30_lg_C = np.sqrt(r30_lg_X*r30_lg_X + r30_lg_r*r30_lg_r)   # end length of side C from cc to bb (mantle side of gen triangle)
    r30_lg_P = r30_lg_A + r30_lg_B + r30_lg_C                   # perimeter of the generating triangle
    r30_n = int(r30_lg_P)     # number of cells is based upon the triangle's estimated largest Perimeter P
    r30 = [0]*r30_n           # we need two lists for the CA: This generation and next generation
    r30nxt = [0]*r30_n

    # either random or something else to initialize the CA
    # for i in range(r30_n): r30[i] = r.randint(0,1)
    r30[int(r30_n/2)] = 1
    btShell = [0]*r30_n            # block types converted from the CA r30[]

    slow_time = -1
    slow_time_modulus = 3
    
    for i in range(nWhorls*tpw):          # 1 revolution every tpw ticks

        slow_time += 1
        if slow_time % slow_time_modulus == 0:
            # produce next generation of the CA
            # indices for 3 adjacent are (relatively) 0 1 2 in the variables ca0 ca1 ca2
            r30nxt = [0]*r30_n

            for j in range(r30_n):
                ca1 = r30[j]
                if j == 0:
                    ca0 = r30[r30_n - 1]
                    ca2 = r30[1]
                elif j == r30_n - 1:
                    ca0 = r30[r30_n - 2]
                    ca2 = r30[0]
                else:
                    ca0 = r30[j-1]
                    ca2 = r30[j+1]
                
                # Rule 30 = 0001 1110 so result is 1 in 4 cases:  001, 010, 011, 100
                if (ca2 == 1 and ca1 == 0 and ca0 == 0) or (ca2 == 0 and not (ca0 == 0 and ca1 == 0)): r30nxt[j] = 1
                # Rule 90 = 0101 1010 and this ignores the cell above; just uses the left and right
                if (ca2 == 1 and ca0 == 0) or (ca2 == 0 and ca0 == 1): r30nxt[j] = 1
                # Serpinski off the top of my head
                # if (ca0 == 0 and ca1 == 1) or (ca0 == 1 and ca1 == 0): r30nxt[j] = 1

                # if j%2 == 1: r30nxt[j] = 1
                
            r30[:] = r30nxt

            # from the CA r30[] produce the corresponding block type list btShell[]
            #   use reduction to expand the scale; it curtails how much of the CA r30[] is used
            reduction = slow_time_modulus
            for j in range(int(r30_n/reduction)):
                for k in range(reduction):
                  if r30[j] == 1: btShell[j*reduction+k] = glass
                  else: btShell[j*reduction+k] = gold

        thetaDeg = float(i)*360.0/float(tpw)
        while thetaDeg > 360.0: thetaDeg -= 360.0     # keep thetaDeg small
        aa.x = origin.x + float(i)*axialRate/float(tpw)
        sideA = geomScale * float(i) + startScale        
        triangleAlt = sideA/dualTanDenom
        sideA_x = triangleAlt/alphaTanDenom
        sideA_X = sideA - sideA_x
        sideB = np.sqrt(sideA_x*sideA_x + triangleAlt*triangleAlt)
        sideC = np.sqrt(sideA_X*sideA_X + triangleAlt*triangleAlt)
        Perim = sideA + sideB + sideC

        # Determine the Euclidean coordinates of vertices cc and bb
        cc.x = aa.x + sideA
        cc.y = aa.y
        cc.z = aa.z
        bb.x = aa.x + triangleAlt/alphaTanDenom
        bb.y = aa.y + triangleAlt * np.cos(thetaDeg*dtr)
        bb.z = aa.z + triangleAlt * np.sin(thetaDeg*dtr) * chirality

        # Transfer the CA r30[] values (map) into the generating triangle (GT)
        #   Strategy 1: map the perimeter of the GT to the full length of the CA
        #   Strategy 2: map the perimeter blocks to the CA blocks so that the distal end of the CA is never referenced by smaller GTs
        #
        # Strategy 1 is something like this...
##        r30_A0 = 0
##        r30_AN = int((sideA/Perim)*r30_n)
##        r30_B0 = r30_AN
##        r30_BN = int(((sideA + sideB)/Perim)*r30_n)
##        r30_C0 = r30_BN
##        r30_CN = r30_n - 1
        #
        # Strategy 2:
        r30_A0 = 0
        r30_AN = int(sideA)
        r30_B0 = r30_AN
        r30_BN = r30_B0 + int(sideB)
        r30_C0 = r30_BN
        r30_CN = r30_C0 + int(sideC)
        

        # Useful diagnostic
        # mc.setBlock(aa.x, aa.y, aa.z, diamond)
        # mc.setBlock(bb.x, bb.y, bb.z, quartz)
        # mc.setBlock(cc.x, cc.y, cc.z + 1, redstone)
        # Also: For monotonic shells use LineSegment(mc, aa, cc, blockType) etcetera
        if drawAxial:
            LineSegmentBTList(mc, aa, cc, btShell[r30_A0:r30_AN])
        if drawApical:
            LineSegmentBTList(mc, aa, bb, btShell[r30_B0:r30_BN])
        if drawMantle:
            LineSegmentBTList(mc, bb, cc, btShell[r30_C0:r30_CN])
    return

# Seashell args: mc, position, whorls, is-sinistral, start-axial, end-axial, axial-rate-per-whorl, include-axial, apex-angle, distal-angle, block type
if seashell:
    # Seashell(mc, c, 3, True, 30.0, 300.0, 10.0, False, 60.0, 30.0, diamond)
    # Seashell(mc, c, 3, True, 30.0, 300.0, 10.0, False, 55.0, 35.0, diamond)
    # Fairly standard:
    # Seashell(mc, c, 3, True, 10.0, 160.0, 6.0, False, 65.0, 25.0, diamond)
    Seashell(mc, c, 2, False, 40., 200., 30.0, False, 55.0, 25.0, diamond)


if groundzero:
    # mc is the minecraft object
    # c is the position with c.x, c.y, c.z
    for k in range(c.z-30, c.z+30):
        for i in range(c.x-30, c.x+30):
            for j in range (c.y, -1, -1):
                mc.setBlock(i, j, k, air)


if clearTheAir:
    clearyoffset = 0
    if clearIncludesPlatform: clearyoffset = ynegoffset
    for i in range(a):
        for j in range(yrange):
            for k in range(a):
                mc.setBlock(c.x+i-a2,c.y+j-clearyoffset,c.z+k-a2,air)
                            
if buildPlatform:
    material = quartz
    for i in range(a):
        for k in range(a):
            mc.setBlock(c.x+i-a2, c.y - 1, c.z+k-a2, platformMaterial)

# This is not quite right: Using c.y makes the mote 1 block high and water flows away from this
#   in both directions... rather than being embedded in the floor at c.y-1
if buildMote:
    for i in range(b2+2,a2-2):
        for k in range(a):
            mc.setBlock(c.x+i, c.y-1, c.z+k-a2, moteMaterial)
            mc.setBlock(c.x-i, c.y-1, c.z+k-a2, moteMaterial)
            mc.setBlock(c.x+k-a2, c.y-1, c.z+i, moteMaterial)
            mc.setBlock(c.x+k-a2, c.y-1, c.z-i, moteMaterial)

if buildTowers:
    print ("towers")
    if airInside:
        print("with air")
    if roof:
        print("with roof")
    for n in range(ntowers):
        s2 = r.randint(tower_minradius, tower_maxradius)
        fs2 = float(s2)
        tower_latx_center = r.randint(c.x-b2+s2,c.x+b2-s2)
        tower_latz_center = r.randint(c.z-b2+s2,c.z+b2-s2)
        tower_low_y = r.randint(towerbottommin, towerbottommax)
        tower_high_y = r.randint(towerymin, towerymax)

        if airInside:
            for yp in range(c.y + tower_low_y, c.y + tower_high_y):
                for radius in range(0,s2):
                    fradius = float(radius)
                    for theta in np.linspace(0, 2.0*pi*fs2, num=7*radius):
                        xp = tower_latx_center + np.cos(theta)*fradius
                        zp = tower_latz_center + np.sin(theta)*fradius
                        mc.setBlock(xp,yp,zp,air)

        # tower wall
        for yp in range(c.y + tower_low_y, c.y+tower_high_y):
            numThetas = int(7*s2)
            for theta in np.linspace(0, 2.0*pi*fs2, num=numThetas):
                xp = tower_latx_center + np.cos(theta)*fs2
                zp = tower_latz_center + np.sin(theta)*fs2
                mc.setBlock(xp,yp,zp,towerMaterial)

        # roof
        if roof:
            yp = c.y + tower_high_y - tower_topfloor_takebacky
            for radius in range(0,s2):
                fradius = float(radius)
                for theta in np.linspace(0, 2.0*pi*fs2, num=7*radius):
                    xp = tower_latx_center + np.cos(theta)*fradius
                    zp = tower_latz_center + np.sin(theta)*fradius
                    mc.setBlock(xp,yp,zp,towerMaterial)

if buildTurrets:
    print("turrets")
    if airInside:
        print("with air")
    if roof:
        print("with roof")

if buildBoxes:
    print("boxes")
    if airInside:
        print("with air")
    if roof:
        print("with roof")


##def ErrorSeashell(mc, pos, nWhorls, isSinistral, startScale, endScale, axialRate, includeAxis, apicalAngleDeg, distalAngleDeg, blockType):
##    if not isSinistral: return
##    drawAxial = False
##    tpw = 100              # integer ticks per whorl
##    origin = mc.player.getPos() # makes origin have type pos, initially at point aa
##    origin.x = pos.x
##    origin.y = pos.y
##    origin.z = pos.z            # makes origin be at the passed location
##    aa = mc.player.getPos() # point of connection sides A and B
##    aa.x = pos.x
##    aa.y = pos.y
##    aa.z = pos.z
##    bb = mc.player.getPos() # sides B and C
##    cc = mc.player.getPos() # sides C and A
##    cc.x = aa.x + startScale
##    cc.y = aa.y
##    cc.z = aa.z
##    dtr = np.arccos(-1.0)/180.0
##    geomScale = (endScale - startScale)/(float(tpw*nWhorls))
##    dualTanDenom = 1.0/np.tan(apicalAngleDeg*dtr) + 1.0/np.tan(distalAngleDeg*dtr)
##    alphaTanDenom = np.tan(apicalAngleDeg*dtr)
##    for i in range(nWhorls*tpw):          # 1 revolution every tpw ticks
##        thetaDeg = float(i)*360.0/float(tpw)
##        while thetaDeg > 360.0: thetaDeg -= 360.0     # keep thetaDeg small
##        aa.x = origin.x + float(i)*axialRate/float(tpw)
##        sideA = geomScale * float(i) + startScale        
##        cc.x = aa.x + sideA
##        triangleAlt = sideA/dualTanDenom
##        bb.x = aa.x + triangleAlt/alphaTanDenom
##        bb.y = triangleAlt * np.cos(thetaDeg*dtr)
##        bb.z = triangleAlt * np.sin(thetaDeg*dtr)
##        if drawAxial:
##            LineSegment(mc, aa, cc, blockType)
##        LineSegment(mc, aa, bb, blockType)
##        LineSegment(mc, bb, cc, blockType) 
##    deltaTheta = 1.0 / (endScale * 2 * pi)
##    return






















