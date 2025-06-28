from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time
import sys
import kilroy
from kilroy import msg

def Pursuit(mc, origin, nV, side, mat, nSteps, dStep, eraseAll, doRandom, do3D):

    if nV > 16:
        print('not really suited to more than 16 bugs with wool... abandon ship')
        return
    
    pursuitDistance = 0.
    foundDistance = False
    
    # create a materials reference either for creating or erasing
    myMat = []
    for i in range(16):
        if eraseAll: myMat.append((0, 0))
        else: myMat.append(mat[i])        

    dtr = np.pi/180.
    rtd = 180./np.pi
    interiorAngleDeg = 360.0/float(nV)
    interiorAngleRad = interiorAngleDeg * dtr
    vertexAngleDeg = 180. - interiorAngleDeg
    vertexAngleRad = np.pi - interiorAngleRad
    halfSide = float(side)/2.0
    halfInteriorAngleRad = interiorAngleRad / 2.
    vertexRadius = halfSide / np.sin(halfInteriorAngleRad)
    
    # corners is a list of positions that will change as we move
    corners = []
    newCorners = []
    if not doRandom:
        for i in range(nV):
            thisPos = mc.player.getPos()
            thisPos.x = origin.x
            thisPos.y = origin.y
            thisPos.z = origin.z
            thisPos.x += vertexRadius * np.cos(float(i)*interiorAngleRad)
            thisPos.z += vertexRadius * np.sin(float(i)*interiorAngleRad)
            corners.append(mc.player.getPos())
            newCorners.append(mc.player.getPos())
            corners[-1].x = thisPos.x
            corners[-1].y = thisPos.y
            corners[-1].z = thisPos.z
            newCorners[-1].x = thisPos.x
            newCorners[-1].y = thisPos.y
            newCorners[-1].z = thisPos.z
    else:
        for i in range(nV):
            thisPos = mc.player.getPos()
            thisPos.x = origin.x
            thisPos.y = origin.y
            thisPos.z = origin.z
            thisPos.x += kilroy.randomBugs[i][0]
            thisPos.z += kilroy.randomBugs[i][2]
            if do3D:
                # this 'take-back' of the origin accommodates the randomBugs[] y-coordinate which
                #   is on the absolute range from 55 to 255
                thisPos.y += kilroy.randomBugs[i][1] - origin.y
            else:
                thisPos.y += 0
            corners.append(mc.player.getPos())
            corners[-1].x = thisPos.x
            corners[-1].y = thisPos.y
            corners[-1].z = thisPos.z
            newCorners.append(mc.player.getPos())
            newCorners[-1].x = thisPos.x
            newCorners[-1].y = thisPos.y
            newCorners[-1].z = thisPos.z

    # create an incremental distance list
    ds = []

    # determine the largest distance between two vertices
    maxDistance = 0.
    for i in range(nV):
        nextIndex = i + 1
        if i == nV - 1: nextIndex = 0
        thisDistance = kilroy.mcdistance(corners[i], corners[nextIndex])
        if thisDistance > maxDistance: maxDistance = thisDistance

    # now establish the ds[] list by scaling each increment by distance / maxDistance
    for i in range(nV):
        nextIndex = i + 1
        if i == nV - 1: nextIndex = 0
        thisDistance = kilroy.mcdistance(corners[i], corners[nextIndex])
        ds.append(dStep*thisDistance/maxDistance)

    for i in range(nSteps):

        # time.sleep(0.01)

        # complete the update and create new blocks before newCorners[] work
        for j in range(nV):
            
            corners[j].x = newCorners[j].x
            corners[j].y = newCorners[j].y
            corners[j].z = newCorners[j].z
            
            mc.setBlock(corners[j].x, corners[j].y, corners[j].z, myMat[j][0], myMat[j][1])

        # calculate the newCorners[] list 
        for j in range(nV):
            
            # now we proceed along the vector from j to k
            k = j + 1
            if k == nV: k = 0
            j2k_x = corners[k].x - corners[j].x
            j2k_y = corners[k].y - corners[j].y
            j2k_z = corners[k].z - corners[j].z

            norm_j2k = kilroy.norm(j2k_x, j2k_y, j2k_z)

            j2k_x = (j2k_x / norm_j2k) * ds[j]
            j2k_y = (j2k_y / norm_j2k) * ds[j]
            j2k_z = (j2k_z / norm_j2k) * ds[j]

            newCorners[j].x = corners[j].x + j2k_x
            newCorners[j].y = corners[j].y + j2k_y
            newCorners[j].z = corners[j].z + j2k_z

        if not foundDistance and kilroy.mcdistance(origin, newCorners[0]) < 1.0:
            foundDistance = True
            pursuitDistance = float(i)*dStep
            cos_arg = np.pi * (1. - 2./float(nV))
            theory = side * (1.0/(1 + np.cos(cos_arg)))
            print ('distance', pursuitDistance, 'w/ side', side, '; at step', i, 'of', nSteps, '; theory says', theory)
            break 
    
mc = Minecraft.create()
xPos, yPos, zPos = 3000, 80, 3000       
mc.player.setPos(xPos, yPos, zPos)

originPos=mc.player.getPos()

originPos.x += 0
originPos.y -= 2

msg(mc, "start pursuit")
tasks = [False, True]

materials = []
for i in range(16): materials.append((kilroy.wool,i))

# minecraft, LLH corner of the lower west hall, [floors, vertices, edges], material, bool erase
nVertices = 16
sideLength = 200
nSteps = 3000
dStep = 0.3
eraseAll = True
doRandom = True
do3D = True
Pursuit(mc, originPos, nVertices, sideLength, materials, nSteps, dStep, eraseAll, doRandom, do3D)
