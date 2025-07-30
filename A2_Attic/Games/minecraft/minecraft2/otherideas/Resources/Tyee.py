from mcpi.minecraft import Minecraft
import numpy as np
import random as r
import time
import kilroy
from kilroy import msg


def TFloor(mc, classCenter, classDimensions, classMaterials):
    kilroy.Floor(mc, classCenter, classDimensions, classMaterials)

def TStairs(mc, schoolPos, wingOffsets, dims, materials):

    nRooms = 4
    
    # landing stages
    stageCenter = mc.player.getPos()
    
    stageCenter.x = schoolPos.x + dims[4]/2
    stageCenter.y = schoolPos.y + wingOffsets[1]/2 + 1
    stageCenter.z = schoolPos.z - dims[4]/2 - wingOffsets[1]/2
    TFloor(mc, stageCenter, [dims[4], 1, dims[4]], materials)
    stageCenter.x = schoolPos.x + dims[4]/2
    stageCenter.y = schoolPos.y + wingOffsets[1]/2 + 1
    stageCenter.z = schoolPos.z - dims[4]/2 + wingOffsets[0] - wingOffsets[1]/2
    TFloor(mc, stageCenter, [dims[5], 1, dims[5]], materials)
    
    stageCenter.x = schoolPos.x + nRooms*dims[1] + (nRooms-1)*dims[3] + dims[4] + dims[5]/2 
    stageCenter.y = schoolPos.y + wingOffsets[1]/2 + 1
    stageCenter.z = schoolPos.z - dims[4]/2 - wingOffsets[1]/2
    TFloor(mc, stageCenter, [dims[4], 1, dims[4]], materials)
    stageCenter.x = schoolPos.x + nRooms*dims[1] + (nRooms-1)*dims[3] + dims[4] + dims[5]/2
    stageCenter.y = schoolPos.y + wingOffsets[1]/2 + 1
    stageCenter.z = schoolPos.z - dims[4]/2 + wingOffsets[0] - wingOffsets[1]/2
    TFloor(mc, stageCenter, [dims[5], 1, dims[5]], materials)

    for j in range(int(wingOffsets[1]/2)+1):
        jcoord = j + schoolPos.y
        kcoord = schoolPos.z - j
        kcoord2 = schoolPos.z - wingOffsets[1]/2 + j

        iJump = nRooms*dims[1] + (nRooms-1)*dims[3] + dims[4]
        for icoord in range(int(schoolPos.x), int(schoolPos.x + 7)):
            # southwest stairs
            mc.setBlock(icoord, jcoord, kcoord, materials[0], materials[1])
            mc.setBlock(icoord + 1 + dims[4]/2, jcoord + wingOffsets[1]/2, kcoord2, materials[0], materials[1])

            # southeast stairs
            mc.setBlock(icoord, jcoord, kcoord + wingOffsets[0], materials[0], materials[1]) 
            mc.setBlock(icoord  + 1 + dims[4]/2, jcoord  + wingOffsets[1]/2, kcoord2 + wingOffsets[0], materials[0], materials[1]) 

            # southwest stairs
            mc.setBlock(icoord + iJump, jcoord, kcoord, materials[0], materials[1])
            mc.setBlock(icoord + 1 + dims[4]/2 + iJump, jcoord + wingOffsets[1]/2, kcoord2, materials[0], materials[1])

            # southeast stairs
            mc.setBlock(icoord + iJump, jcoord, kcoord + wingOffsets[0], materials[0], materials[1]) 
            mc.setBlock(icoord  + 1 + dims[4]/2 + iJump, jcoord  + wingOffsets[1]/2, kcoord2 + wingOffsets[0], materials[0], materials[1]) 

def Dot(mc, x, y, z, radius, materials):
    dotX = int(x)
    dotY = int(y)
    dotZ = int(z)
    dotR = int(radius)
    for i in range(dotX - radius, dotX + radius + 1):
        for k in range(dotZ - radius, dotZ + radius + 1):
            dx = float(dotX - i)
            dz = float(dotZ - k)
            d = np.sqrt(dx*dx + dz*dz)
            if d <= float(dotR):
                mc.setBlock(i, y, k, materials[2], materials[3])
    
    
def TWing(mc, schoolPos, whichWing, wingOffsets, nRooms, dims, materials):
    # mc is a pass-through
    # schoolPos and whichWing gives us wingPos
    wingPos = mc.player.getPos()
    wingPos.x = schoolPos.x
    wingPos.y = schoolPos.y
    wingPos.z = schoolPos.z
    if whichWing[1] == True: wingPos.y += wingOffsets[1]
    if whichWing[0] == True: wingPos.z += wingOffsets[0]
    zHall = dims[0]
    xClass = dims[1]
    zClass = dims[2]
    xIntraClass = dims[3]
    xSVest = dims[4]         # vestibule is the extensions at N and S ends of the hall
    xNVest = dims[5]

    # length of the central hallway
    hallLength = nRooms*xClass + (nRooms-1)*xIntraClass + xSVest + xNVest

    # Get the center of the hallway
    hallCenterPos = mc.player.getPos()
    hallCenterPos.x = wingPos.x + int(hallLength / 2)
    hallCenterPos.y = wingPos.y
    hallCenterPos.z = wingPos.z + int(zHall/2)

    justFloorsTask = [True, False, False, False, False, False]

    # hallway
    TFloor(mc, hallCenterPos, [hallLength, 1, zHall], materials)

    # Classrooms
    # sides of hallway
    for side in range(2):
        # classrooms along side
        for classroom in range(nRooms):
            classPos = mc.player.getPos()
            classPos.x = wingPos.x + xSVest + classroom * (xClass + xIntraClass) + int(xClass/2)
            classPos.y = wingPos.y
            classPos.z = wingPos.z - zClass + side * (zClass + zHall) + int(zClass/2)
            # make the classroom floor
            TFloor(mc, classPos, [xClass, 1, zClass], materials)

def BuildTyee(mc, schoolPos, tasks, materials, erase):
    print('build Tyee')
    choice = [False, True]
    wingOffsets = [101, 41]
    nRooms = 4
    buildWings = tasks[0]
    makeTiles = tasks[1]
    zHall = 11
    zClass = 29
    xClass = 29
    xDClass = 7
    sVestX = 15
    nVestX = 15
    dims = [zHall, xClass, zClass, xDClass, sVestX, nVestX]

    # Hah this is clever: If we are erasing tiles we make them quartz.
    #   If we are erasing floors we make them air
    if erase: materials = [air, 0, quartz, 0]
    
    if buildWings: 
        for west in choice:
            for floor in choice:
                TWing(mc, schoolPos, [west, floor], wingOffsets, nRooms, dims, materials)

        print('now building stairs between wings')
        TStairs(mc, schoolPos, wingOffsets, dims, materials)

        # Atrium
        atriumPos = mc.player.getPos()
        atriumPos.x = schoolPos.x - 27
        atriumPos.y = schoolPos.y
        atriumPos.z = schoolPos.z - 10 + 65
        TFloor(mc, atriumPos, [55, 1, 131], materials)

        # Upper floor connector hallway
        ufchPos = mc.player.getPos()
        ufchPos.x = schoolPos.x - 5
        ufchPos.y = schoolPos.y + wingOffsets[1]
        ufchPos.z = schoolPos.z + 56
        TFloor(mc, ufchPos, [9, 1, 112], materials)
    
    if makeTiles:
        radius = 3
        lunchRelX = -41
        lunchRelZ = 9
        wingDeltaY = wingOffsets[1]
        wingDeltaZ = wingOffsets[0]
        for dz in [0, wingDeltaZ]:

            deltaStaircaseX = sVestX + 4*xClass + 3*xDClass + 3
            for stairX in [schoolPos.x + 3, schoolPos.x + deltaStaircaseX]:
                # welcome to level 0 (dy = 0) with dz = 0 and 101
                # Here let's do the paths *Up* both staircases
                aUp = mc.player.getPos()
                bUp = mc.player.getPos()
                # path from center of hall to base of stairs
                aUp.x, aUp.y, aUp.z = stairX, schoolPos.y, schoolPos.z + int(zHall/2) + dz
                bUp.x, bUp.y, bUp.z = aUp.x, schoolPos.y, schoolPos.z + dz
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # path up first flight
                aUp.x, aUp.y, aUp.z = bUp.x, schoolPos.y + int(wingDeltaY/2) + 1, schoolPos.z - int(wingDeltaY/2) - 1 + dz
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # path top of stairs onto landing
                bUp.x, bUp.y, bUp.z = aUp.x, aUp.y, aUp.z - 7
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # north-south leg of landing path
                aUp.x, aUp.y, aUp.z = bUp.x + 8, bUp.y, bUp.z
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # landing back east to second flight
                bUp.x, bUp.y, bUp.z = aUp.x, aUp.y, aUp.z + 8 
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # path up second flight
                aUp.x, aUp.y, aUp.z = bUp.x, bUp.y + int(wingDeltaY/2), bUp.z + int(wingDeltaY/2)
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

                # top of second flight to center of hall
                bUp.x, bUp.y, bUp.z = aUp.x, aUp.y, aUp.z + int(zHall/2)
                kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

            
            for dy in [0, wingDeltaY]:

                # welcome to the wing with (dy, dz)

                # vertices at five points along the hall
                hallX0 = schoolPos.x + 3
                if dy == wingDeltaY: hallX0 += 8
                hallX1 = schoolPos.x + sVestX + int(xClass/2)
                hallX2 = hallX1 + xClass + xDClass
                hallX3 = hallX2 + xClass + xDClass
                hallX4 = hallX3 + xClass + xDClass
                for hallVertX in [hallX0, hallX1, hallX2, hallX3, hallX4]:
                    Dot(mc, hallVertX, schoolPos.y + dy, schoolPos.z + dz + zHall/2, radius, materials)

                # vertices in the four classrooms, both sides of the hall
                classX1 = schoolPos.x + sVestX + int(xClass/2)
                classX2 = classX1 + xClass + xDClass
                classX3 = classX2 + xClass + xDClass
                classX4 = classX3 + xClass + xDClass
                classZ1 = schoolPos.z - int(zClass/2)
                classZ2 = classZ1 + zClass + zHall
                for classVertX in [classX1, classX2, classX3, classX4]:
                    # crossing edges
                    for z in range(zClass + zHall + 1):
                        mc.setBlock(classVertX, schoolPos.y + dy, classZ1 + z + dz, materials[2], materials[3]) 
                    # vertices
                    for classVertZ in [classZ1, classZ2]:
                        Dot(mc, classVertX, schoolPos.y + dy, classVertZ + dz, radius, materials)

                # longitudinal stripes
                endStripeX = int(hallX4) + 19
                if dy == wingDeltaY: endStripeX += 7
                for i in range(int(hallX0), endStripeX):
                    mc.setBlock(i, schoolPos.y + dy, schoolPos.z + dz + zHall/2, materials[2], materials[3])

        # vertex in lunchroom
        Dot(mc, schoolPos.x + lunchRelX, schoolPos.y, schoolPos.z + lunchRelZ, radius, materials)

        # upper level connector
        aUp.x, aUp.y, aUp.z = schoolPos.x + 11, schoolPos.y + wingDeltaY, schoolPos.z + 5
        bUp.x, bUp.y, bUp.z = aUp.x - 16, aUp.y, aUp.z  
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        aUp.x, aUp.y, aUp.z = bUp.x, bUp.y, bUp.z + wingDeltaZ
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        bUp.x, bUp.y, bUp.z = aUp.x + 16, aUp.y, aUp.z
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

        # lower level connector
        aUp.x, aUp.y, aUp.z = schoolPos.x + 4, schoolPos.y, schoolPos.z + 5
        bUp.x, bUp.y, bUp.z = aUp.x - 7, aUp.y, aUp.z  
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        aUp.x, aUp.y, aUp.z = bUp.x, bUp.y, bUp.z + wingDeltaZ
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        bUp.x, bUp.y, bUp.z = aUp.x + 11, aUp.y, aUp.z
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

        # lower level to lunch west vestibule vertex
        aUp.x, aUp.y, aUp.z = schoolPos.x + 4, schoolPos.y, schoolPos.z + 5
        bUp.x, bUp.y, bUp.z = aUp.x - 7, aUp.y, aUp.z - 7  
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        aUp.x, aUp.y, aUp.z = schoolPos.x + lunchRelX, schoolPos.y, schoolPos.z + lunchRelZ
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])

        # lower level to lunch east vestibule vertex
        aUp.x, aUp.y, aUp.z = schoolPos.x + 4, schoolPos.y, schoolPos.z + 5 + wingDeltaZ
        bUp.x, bUp.y, bUp.z = aUp.x - 7, aUp.y, aUp.z + 7  
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        aUp.x, aUp.y, aUp.z = schoolPos.x + lunchRelX, schoolPos.y, schoolPos.z + lunchRelZ
        kilroy.LineSegment(mc, aUp, bUp, materials[2], materials[3])
        

mc = Minecraft.create()
xPos, yPos, zPos = 1680, 80, 2000       
mc.player.setPos(xPos, yPos, zPos)


sPos=mc.player.getPos()
sPos.x += 0
sPos.y -= 2

msg(mc, "startTyee")
tasks = [False, True]

materials = [quartz, 0, wool, 2]

print(sPos.x, sPos.y, sPos.z)

# minecraft, LLH corner of the lower west hall, [floors, vertices, edges], material, bool erase
BuildTyee(mc, sPos, tasks, materials, False)







